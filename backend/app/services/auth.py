from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.core import security

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate):
    hashed_pw = security.hash_password(user.password)
    db_user = User(
        email=user.email,
        hashed_password=hashed_pw,
        full_name=user.full_name,
        role=user.role,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user