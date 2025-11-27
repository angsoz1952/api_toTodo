from repository.user_repository import get_by_username_repository, create_user_repository
from sqlalchemy.orm import Session
from schemas.user import UserCreate
from uitls.hashing import hash_password, verify_password
from uitls.jwt import create_access_token

class UserService:
   
   @staticmethod
   def register_user(db: Session, user_create: UserCreate):
      existing_user = get_by_username_repository(user_create.username, db)
      if existing_user:
         return None
      hashed_pwd = hash_password(user_create.password)
      return create_user_repository(user_create.username, hashed_pwd, db)

   @staticmethod
   def authenticate_user(db: Session, username: str, password: str):
      user = get_by_username_repository(username, db)
      if user and verify_password(password, user.password):
         return user
      return None
   
   @staticmethod
   def generate_token(user_id: int, username: str):
      return create_access_token({"sub": username, "user_id": user_id})