import bcrypt
import jwt
from datetime import datetime, timedelta
from fastapi import HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from .models import User, Role

SECRET_KEY = "your_secret_key"  # replace with os.getenv in production
security = HTTPBearer()

USER_DATABASE = {
    "finance_user": {
        "hashed_password": bcrypt.hashpw("finance_pass".encode(), bcrypt.gensalt()),
        "user": User(username="finance_user", role=Role.FINANCE, department="Finance")
    },
    "marketing_user": {
        "hashed_password": bcrypt.hashpw("marketing_pass".encode(), bcrypt.gensalt()),
        "user": User(username="marketing_user", role=Role.MARKETING, department="Marketing")
    },
    "hr_user": {
        "hashed_password": bcrypt.hashpw("hr_pass".encode(), bcrypt.gensalt()),
        "user": User(username="hr_user", role=Role.HR, department="HR")
    },
    "eng_user": {
        "hashed_password": bcrypt.hashpw("eng_pass".encode(), bcrypt.gensalt()),
        "user": User(username="eng_user", role=Role.ENGINEERING, department="Engineering")
    },
    "ceo_user": {
        "hashed_password": bcrypt.hashpw("ceo_pass".encode(), bcrypt.gensalt()),
        "user": User(username="ceo_user", role=Role.CEO)
    },
    "employee_user": {
        "hashed_password": bcrypt.hashpw("employee_pass".encode(), bcrypt.gensalt()),
        "user": User(username="employee_user", role=Role.EMPLOYEE)
    }
}

def authenticate_user(username: str, password: str):
    if username not in USER_DATABASE:
        return None
    user_info = USER_DATABASE[username]
    if bcrypt.checkpw(password.encode(), user_info["hashed_password"]):
        return user_info["user"]
    return None

def create_token(user: User):
    payload = {
        "sub": user.username,
        "role": user.role.value,
        "exp": datetime.utcnow() + timedelta(hours=2)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        username = payload.get("sub")
        if username not in USER_DATABASE:
            raise HTTPException(status_code=401, detail="Invalid token")
        return USER_DATABASE[username]["user"]
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

async def get_current_user(credentials: HTTPAuthorizationCredentials = Security(security)) -> User:
    return decode_token(credentials.credentials)
