from ninja.security import HttpBearer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, AuthenticationFailed

class NinjaJWTAuth(HttpBearer):
    def authenticate(self, request, token):
        auth = JWTAuthentication()
        try:
            # Validate the token using SimpleJWT
            validated_token = auth.get_validated_token(token)
            # Return the user associated with the token
            return auth.get_user(validated_token)
        except (InvalidToken, AuthenticationFailed):
            return None
