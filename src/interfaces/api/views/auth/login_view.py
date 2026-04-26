from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from src.interfaces.api.serializers.auth.login_serializer import LoginSerializer
from src.application.use_cases.auth.login import LoginUseCase
from src.infrastructure.db.repositories.user_repository_impl import DjangoUserRepository
from src.infrastructure.auth.hash_service_impl import BcryptHashService
from src.infrastructure.auth.jwt_service_impl import SimpleJwtService
from src.application.exceptions import InvalidCredentialsException

class LoginView(APIView):
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        use_case = LoginUseCase(
            user_repo=DjangoUserRepository(),
            hash_service=BcryptHashService(),
            jwt_service=SimpleJwtService()
        )
        
        try:
            
            result = use_case.execute(data=serializer.validated_data)
            return Response(result, status=status.HTTP_200_OK)
            
        except InvalidCredentialsException as e:
            return Response(
                {
                    "error": {
                        "code": "invalid_credential",
                        "message": "Invalid email or password"
                    }
                },
                status=status.HTTP_401_UNAUTHORIZED
            )
        
