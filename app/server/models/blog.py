from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from datetime import  datetime
from pydbantic import PrimaryKey
# from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,DateTime
# from sqlalchemy.orm import relationship
# from sqlalchemy_utils import EmailType,URLType
import datetime

#model for the user schema 
class UserSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "email": "jdoe@x.edu.ng",
                "password": "Suchandra@123",
            }
        }

#model for the user schema update
class UpdateuserModel(BaseModel):
    fullname: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "email": "jdoe@x.edu.ng",
                "password": "Suchandra@123",
            }
        }

#model for the Post schema 
class PostSchema(BaseModel):
    title : str = Field(...)
    body: str = Field(...)

#model for the Post schema update
class UpdatePostModel(BaseModel):
    title: Optional[str]
    body: Optional[str]

#model for the Comment schema 
class CommentSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    body: str = Field(...)


#model for response
def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

#model for error
def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
