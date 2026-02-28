from ninja import Schema
from pydantic import Field

class TokenObtainPairSchema(Schema):
    username: str
    password: str

class TokenRefreshSchema(Schema):
    refresh: str

class TokenPairOutSchema(Schema):
    access: str
    refresh: str

class ErrorSchema(Schema):
    detail: str
