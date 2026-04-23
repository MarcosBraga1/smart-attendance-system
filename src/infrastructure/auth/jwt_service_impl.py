from src.domain.services.jwt_service import JwtService
from rest_framework_simplejwt.tokens import RefreshToken

class SimpleJwtService(JwtService):
    
    def generate_token(self, user):
        refresh = RefreshToken.for_user(user)
        
        refresh["role"] = user.role
        
        return {
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh)
        }