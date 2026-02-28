from ninja import Router
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .schemas import TokenObtainPairSchema, TokenRefreshSchema, TokenPairOutSchema, ErrorSchema

router = Router(tags=["Auth"])

@router.post("/login", response={200: TokenPairOutSchema, 401: ErrorSchema})
def login_view(request, data: TokenObtainPairSchema):
    user = authenticate(username=data.username, password=data.password)
    if user is None:
        return 401, {"detail": "Invalid credentials"}
    
    refresh = RefreshToken.for_user(user)
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }

@router.post("/refresh", response={200: TokenPairOutSchema, 401: ErrorSchema})
def refresh_view(request, data: TokenRefreshSchema):
    try:
        refresh = RefreshToken(data.refresh)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
    except Exception as e:
        return 401, {"detail": "Invalid refresh token"}
