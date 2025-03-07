from pydantic import BaseModel, ConfigDict
from datetime import datetime

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)
