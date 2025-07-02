from sqlalchemy import Column, Integer, String, Enum
from app.core.database import Base
import enum

class UserRole(str, enum.Enum):
    client = "client"
    admin = "admin"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, nullable=True)
    role = Column(Enum(UserRole), default=UserRole.client, nullable=False)
