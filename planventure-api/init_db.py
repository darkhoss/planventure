from app import create_app, db
from models import User, Trip

def create_tables():
    app = create_app()
    """Create all database tables"""
    with app.app_context():
        print("Registered models:", db.Model.registry.mappers)
        db.create_all()
        print("✅ Database tables created successfully!")

def reset_tables():
    """Drop all tables and recreate them"""
    with app.app_context():
        db.drop_all()
        db.create_all()
        print("✅ Database tables reset successfully!")

if __name__ == "__main__":
    # You can run this directly with: python create_tables.py
    create_tables()