from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from src.interfaces.api.permissions.is_professor_or_admin import IsProfessorOrAdmin
from src.interfaces.api.serializers.professor.create_professor_serializer import CreateProfessorSerializer
from src.interfaces.api.serializers.professor.professor_response_serializer import ProfessorResponseSerializer
from src.interfaces.api.serializers.professor.update_professor_serializer import UpdateProfessorSerializer
from src.application.use_cases.professor.create_professor import CreateProfessorUseCase
from src.application.use_cases.professor.delete_professor import DeleteProfessorUseCase
from src.application.use_cases.professor.get_professor import GetProfessorUseCase
from src.application.use_cases.professor.list_professors import ListProfessorsUseCase
from src.application.use_cases.professor.update_professor import UpdateProfessorUseCase
from src.application.exceptions import AlreadyExistsException, NotFoundException, PermissionDeniedException
from src.infrastructure.db.repositories.user_repository_impl import DjangoUserRepository
from src.infrastructure.db.repositories.professor_repository_impl import DjangoProfessorRepository
from src.infrastructure.auth.hash_service_impl import BcryptHashService

class ProfessorViewSet(ViewSet):
    
    permission_classes = [IsAuthenticated, IsProfessorOrAdmin]
    
    def create(self, request):
        serializer = CreateProfessorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        use_case = CreateProfessorUseCase(
            user_repo=DjangoUserRepository(),
            professor_repo=DjangoProfessorRepository(),
            hash_service=BcryptHashService()
        )
        
        try:
            
            result = use_case.execute(data=serializer.validated_data)
            
            serializer = ProfessorResponseSerializer(result)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        except AlreadyExistsException as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        use_case = ListProfessorsUseCase(
            professor_repo=DjangoProfessorRepository()
        )
        
        professors = use_case.execute()
        
        serializer = ProfessorResponseSerializer(professors, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        use_case = GetProfessorUseCase(
            professor_repo=DjangoProfessorRepository()
        )
        
        try:
            
            professor = use_case.execute(professor_id=pk, user=request.user)
            
            serializer = ProfessorResponseSerializer(professor)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except NotFoundException:
            return Response(
                {
                    "error": {
                        "code": "404_not_found",
                        "message": "Professor not found"
                    }
                }, status=status.HTTP_404_NOT_FOUND
            )
            
        except PermissionDeniedException:
            return Response(
                {
                    "error": {
                        "code": "403_forbidden",
                        "message": "Not allowed"
                    }
                }
            )
    
    def update(self, request, pk=None):
        serializer = UpdateProfessorSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        
        use_case = UpdateProfessorUseCase(
            professor_repo=DjangoProfessorRepository()
        )
        
        try:
            
            professor = use_case.execute(professor_id=pk, data=serializer.validated_data, user=request.user)
            
            serializer = ProfessorResponseSerializer(professor)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except NotFoundException:
            return Response(
                {
                    "error": {
                        "code": "404_not_found",
                        "message": "Professor not found"
                    }
                }, status=status.HTTP_404_NOT_FOUND
            )
            
        except PermissionDeniedException:
            return Response(
                {
                    "error": {
                        "code": "403_forbidden",
                        "message": "Not allowed"
                    }
                }, status=status.HTTP_403_FORBIDDEN
            )
    
    def destroy(self, request, pk=None):
        use_case = DeleteProfessorUseCase(
            professor_repo=DjangoProfessorRepository()
        )
        
        try:
            
            use_case.execute(professor_id=pk, user=request.user)
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        except NotFoundException:
            return Response(
                {
                    "error": {
                        "code": "404_not_found",
                        "message": "Professor not found"
                    }
                }, status=status.HTTP_404_NOT_FOUND
            )
            
        except PermissionDeniedException:
            return Response(
                {
                    "error": {
                        "code": "403_forbidden",
                        "message": "Not allowed"
                    }
                }, status=status.HTTP_403_FORBIDDEN
            )