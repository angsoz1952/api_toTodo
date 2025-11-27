from service.user_service import UserService
from fastapi import APIRouter, Depends, status, HTTPException
from schemas.user import UserCreate, UserResponse, LoginRequest, TokenResponse
from database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register_user(user_create: UserCreate, db: Session = Depends(get_db)):
    user = UserService.register_user(db, user_create)
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already registered")
    return user

@router.post("/login", response_model=TokenResponse, status_code=status.HTTP_200_OK)
def login_user(login_data: LoginRequest, db: Session = Depends(get_db)): 
    user = UserService.authenticate_user(db, login_data.username, login_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")
    token = UserService.generate_token(user.id, user.username)
    return TokenResponse(access_token=token, token_type="bearer", user=user)