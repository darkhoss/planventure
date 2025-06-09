from app import db
from datetime import datetime, timezone
from email_validator import validate_email, EmailNotValidError
from utils.auth import hash_password, verify_password
from .mixins import TimestampMixin

class User(db.Model, TimestampMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.LargeBinary(60), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    last_login = db.Column(db.DateTime)

    # Relationship
    trips = db.relationship('Trip', backref='user', lazy=True)

    def __init__(self, email, password):
        self.email = self.validate_email(email)
        self.set_password(password)

    @staticmethod
    def validate_email(email):
        try:
            valid = validate_email(email)
            return valid.email
        except EmailNotValidError:
            raise ValueError('Invalid email address')

    def set_password(self, password):
        """Set the user's password hash"""
        self.password_hash = hash_password(password)

    def check_password(self, password):
        """Verify the user's password"""
        return verify_password(password, self.password_hash)

    def __repr__(self):
        return f'<User {self.email}>'