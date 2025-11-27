from models.user import User
from sqlalchemy.orm import Session

def get_by_username_repository(username: str, db: Session):
   return db.query(User).filter(User.username == username).first()

def create_user_repository(username: str, hashed_password: str, db: Session):
    new_user = User(username=username, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
