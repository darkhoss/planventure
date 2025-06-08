from app import db
from datetime import datetime, timezone
from email_validator import validate_email, EmailNotValidError

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    last_login = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    trips = db.relationship('Trip', backref='owner', lazy=True)

    def __init__(self, email, password_hash):
        self.email = self.validate_email(email)
        self.password_hash = password_hash

    @staticmethod
    def validate_email(email):
        try:
            valid = validate_email(email)
            return valid.email
        except EmailNotValidError:
            raise ValueError('Invalid email address')

    def __repr__(self):
        return f'<User {self.email}>'