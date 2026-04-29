from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from src.interfaces.api.permissions.is_professor_or_admin import IsProfessorOrAdmin
from src.interfaces.api.serializers.class_session.class_session_response_serializer import ClassSessionResponseSerializer
from src.interfaces.api.serializers.class_session.create_class_session_serializer import CreateClassSessionSerializer
from src.interfaces.api.serializers.class_session.update_class_session_serializer import UpdateClassSessionSerializer
from src.application.use_cases.class_session.create_class_session import CreateClassSessionUseCase
from src.application.use_cases.class_session.delete_class_session import DeleteClassSessionUseCase
from src.application.use_cases.class_session.get_class_session import GetClassSessionUseCase
from src.application.use_cases.class_session.list_class_session import ListClassSessionUseCase
from src.application.use_cases.class_session.update_class_session import UpdateClassSessionUseCase
from src.application.exceptions import NotFoundException, PermissionDeniedException
from src.infrastructure.db.repositories.class_session_repository_impl import DjangoClassSessionRepository
from src.infrastructure.db.repositories.discipline_repository_impl import DjangoDisciplineRepository
from src.infrastructure.db.repositories.room_repository_impl import DjangoRoomRepository

class ClassSessionViewSet(ViewSet):
    
    permission_classes = [IsAuthenticated, IsProfessorOrAdmin]
    
    def create(self, request):
        serializer = CreateClassSessionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        use_case = CreateClassSessionUseCase(
            class_session_repo=DjangoClassSessionRepository(),
            discipline_repo=DjangoDisciplineRepository(),
            room_repo=DjangoRoomRepository()
        )
        
        try:
            
            result = use_case.execute(data=serializer.validated_data)
            
            serializer = ClassSessionResponseSerializer(result)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        except NotFoundException:
            return Response(
                {
                    "error": {
                        "code": "404_not_found",
                        "message": "Discipline or room not found"
                    }
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def list(self, request):
        use_case = ListClassSessionUseCase(
            class_session_repo=DjangoClassSessionRepository()
        )
        
        class_sessions = use_case.execute()
        
        serializer = ClassSessionResponseSerializer(class_sessions, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        use_case = GetClassSessionUseCase(
            class_session_repo=DjangoClassSessionRepository()
        )
        
        try:
            
            class_session = use_case.execute(class_session_id=pk)
            
            serializer = ClassSessionResponseSerializer(class_session)
            
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
    
    def update(self, request, pk=None):
        serializer = UpdateClassSessionSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        
        use_case = UpdateClassSessionUseCase(
            class_session_repo=DjangoClassSessionRepository()
        )
        
        try:
            
            class_session = use_case.execute(class_session_id=pk, data=serializer.validated_data, user=request.user)
            
            serializer = ClassSessionResponseSerializer(class_session)
            
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
        use_case = DeleteClassSessionUseCase(
            class_session_repo=DjangoClassSessionRepository()
        )
        
        try:
            
            use_case.execute(class_session_id=pk, user=request.user)
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