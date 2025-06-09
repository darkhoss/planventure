from flask import Blueprint, request, jsonify
from app import db
from models import User
from utils.validation import validate_email_format
import bcrypt

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({'error': 'Email and password are required'}), 400

    try:
        # Validate and normalize email
        email = validate_email_format(data['email'])

        # Check if user already exists
        if User.query.filter_by(email=email).first():
            return jsonify({'error': 'Email already registered'}), 409

        # Create new user
        new_user = User(
            email=email,
            password=data['password']
        )
        
        db.session.add(new_user)
        db.session.commit()

        return jsonify({
            'message': 'User registered successfully',
            'user_id': new_user.id
        }), 201

    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Registration failed'}), 500
