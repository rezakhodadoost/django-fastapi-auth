import fastapi
import pydantic

from sqlalchemy.orm import Session
from fastapi import Depends

from database import get_db
from models import User

from pwdlib import PasswordHash


app = fastapi.FastAPI()

password_hash = PasswordHash.recommended()


class RegisterRequest(pydantic.BaseModel):
    username: str
    password: str


@app.post("/register/")
def register(
    data: RegisterRequest,
    db: Session = Depends(get_db)
):

    existing_user = (
        db.query(User)
        .filter(User.username == data.username)
        .first()
    )

    if existing_user:
        raise fastapi.HTTPException(
            status_code=400,
            detail="username already exists"
        )

    hashed_password = password_hash.hash(data.password)

    new_user = User(
        username=data.username,
        password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "user created successfully",
        "username": new_user.username
    }


class LoginRequest(pydantic.BaseModel):
    username: str
    password: str


@app.post("/login/")
def login(
    data: LoginRequest,
    db: Session = Depends(get_db)
):

    user = (
        db.query(User)
        .filter(User.username == data.username)
        .first()
    )

    if not user:
        raise fastapi.HTTPException(
            status_code=401,
            detail="invalid username or password"
        )

    if not password_hash.verify(data.password, user.password):
        raise fastapi.HTTPException(
            status_code=401,
            detail="invalid username or password"
        )

    return {
        "message": "Login successful",
        "username": user.username
    }