from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from src.interfaces.api.permissions.is_professor_or_admin import IsProfessorOrAdmin
from src.interfaces.api.serializers.discipline.create_discipline_serializer import CreateDisciplineSerializer
from src.interfaces.api.serializers.discipline.discipline_response_serializer import DisciplineResponseSerializer
from src.interfaces.api.serializers.discipline.update_discipline_serializer import UpdateDisciplineSerializer
from src.application.use_cases.discipline.create_discipline import CreateDisciplineUseCase
from src.application.use_cases.discipline.delete_discipline import DeleteDisciplineUseCase
from src.application.use_cases.discipline.get_discipline import GetDisciplineUseCase
from src.application.use_cases.discipline.list_discipline import ListDisciplineUseCase
from src.application.use_cases.discipline.update_discipline import UpdateDisciplineUseCase
from src.application.exceptions import NotFoundException, PermissionDeniedException
from src.infrastructure.db.repositories.discipline_repository_impl import DjangoDisciplineRepository
from src.infrastructure.db.repositories.professor_repository_impl import DjangoProfessorRepository

class DisciplineViewSet(ViewSet):
    
    permission_classes = [IsAuthenticated, IsProfessorOrAdmin]
    
    def create(self, request):
        serializer = CreateDisciplineSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        use_case = CreateDisciplineUseCase(
            discipline_repo=DjangoDisciplineRepository(),
            professor_repo=DjangoProfessorRepository()
        )
        
        try:
            
            result = use_case.execute(data=serializer.validated_data)
            
            serializer = DisciplineResponseSerializer(result)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        except NotFoundException:
            return Response(
                {
                    "error": {
                        "code": "404_not_found",
                        "message": "Professor not found"
                    }
                }, status=status.HTTP_404_NOT_FOUND
            )
    
    def list(self, request):
        use_case = ListDisciplineUseCase(
            discipline_repo=DjangoDisciplineRepository()
        )
        
        disciplines = use_case.execute()
        
        serializer = DisciplineResponseSerializer(disciplines, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        use_case = GetDisciplineUseCase(
            discipline_repo=DjangoDisciplineRepository()
        )
        
        try:
            
            discipline = use_case.execute(discipline_id=pk)
            
            serializer = DisciplineResponseSerializer(discipline)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except NotFoundException:
            return Response(
                {
                    "error": {
                        "code": "404_not_found",
                        "message": "Discipline not found"
                    }
                }, status=status.HTTP_404_NOT_FOUND
            )
    
    def update(self, request, pk=None):
        serializer = UpdateDisciplineSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        
        use_case = UpdateDisciplineUseCase(
            discipline_repo=DjangoDisciplineRepository()
        )
        
        try:
            
            discipline = use_case.execute(discipline_id=pk, data=serializer.validated_data, user=request.user)
            
            serializer = DisciplineResponseSerializer(discipline)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except NotFoundException:
            return Response(
                {
                    "error": {
                        "code": "404_not_found",
                        "message": "Discipline not found"
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
        use_case = DeleteDisciplineUseCase(
            discipline_repo=DjangoDisciplineRepository()
        )
        
        try:
            
            use_case.execute(discipline_id=pk, user=request.user)
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        except NotFoundException:
            return Response(
                {
                    "error": {
                        "code": "404_not_found",
                        "message": "Discipline not found"
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