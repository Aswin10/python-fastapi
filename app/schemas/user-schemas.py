from typing import Optional
from pydantic import BaseModel, EmailStr



class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Optional[str] = None