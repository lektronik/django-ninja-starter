from ninja import Router
from django.contrib.auth.models import User
from django.db import IntegrityError
from .schemas import RegisterSchema, UserOutSchema, ErrorSchema

router = Router(tags=["Auth"])

@router.post("/register", response={201: UserOutSchema, 400: ErrorSchema})
def register_view(request, data: RegisterSchema):
    try:
        # Basic validation
        if User.objects.filter(username=data.username).exists():
            return 400, {"detail": "Username already exists"}
            
        user = User.objects.create_user(
            username=data.username,
            email=data.email,
            password=data.password
        )
        return 201, user
    except Exception as e:
        return 400, {"detail": str(e)}
