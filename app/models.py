from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

class Role(str, Enum):
    FINANCE = "finance"
    MARKETING = "marketing"
    HR = "hr"
    ENGINEERING = "engineering"
    CEO = "ceo"
    EMPLOYEE = "employee"

class User(BaseModel):
    username: str
    role: Role
    department: Optional[str] = None

class Query(BaseModel):
    text: str

class Response(BaseModel):
    answer: str
    sources: List[str]
    role: str
