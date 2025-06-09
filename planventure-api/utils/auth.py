from flask_jwt_extended import create_access_token, get_jwt_identity
from datetime import timedelta

def generate_token(user_id):
    """Generate a JWT token for the given user ID"""
    expires = timedelta(days=1)
    token = create_access_token(
        identity=user_id,
        expires_delta=expires,
        additional_claims={"type": "access"}
    )
    return token

def get_current_user_id():
    """Get the current user's ID from the JWT token"""
    return get_jwt_identity()
import bcrypt

def hash_password(password: str) -> bytes:
    """Hash a password using bcrypt"""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)

def verify_password(password: str, hashed_password: bytes) -> bool:
    """Verify a password against a hash"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
