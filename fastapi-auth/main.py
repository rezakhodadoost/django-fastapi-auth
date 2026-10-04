import fastapi
import pydantic

app = fastapi.FastAPI()

users = {}


class RegisterRequest(pydantic.BaseModel):
    username: str
    password: str


@app.post("/register/")
def register(data: RegisterRequest):

    if data.username in users:
        return fastapi.HTTPException(
            status_code=400,
            detail="username already exists"
        )

    users[data.username] = data.password

    return {
        "message": "user created successfully",
        "username": data.username
    }


class LoginRequest(pydantic.BaseModel):
    username: str
    password: str


@app.post("/login/")
def login(data: LoginRequest):

    if data.username not in users:
        raise fastapi.HTTPException(
            status_code=401,
            detail="invalid username or password"
        )

    if users[data.username] != data.password:
        raise fastapi.HTTPException(
            status_code=401,
            detail="invalid username or password"
        )

    return {
        "message": "Login successful",
        "username": data.username
    }