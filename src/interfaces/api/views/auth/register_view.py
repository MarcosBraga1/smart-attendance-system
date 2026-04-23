from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from src.interfaces.api.serializers.auth.register_serializer import RegisterSerializer
from src.application.use_cases.register_user import RegisterUserUseCase
from src.application.exceptions import AlreadyExistsException
from src.infrastructure.db.repositories.user_repository_impl import DjangoUserRepository
from src.infrastructure.db.repositories.student_repository_impl import DjangoStudentRespository
from src.infrastructure.db.repositories.professor_repository_impl import DjangoProfessorRepository
from src.infrastructure.auth.hash_service_impl import BcryptHashService

class RegisterView(APIView):
    
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        use_case = RegisterUserUseCase(
            user_repo=DjangoUserRepository(),
            student_repo=DjangoStudentRespository(),
            professor_repo=DjangoProfessorRepository(),
            hash_service=BcryptHashService()
        )
        
        try:
            
            result = use_case.execute(serializer.validated_data)
            return Response(result, status=status.HTTP_201_CREATED)
        
        except AlreadyExistsException as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)