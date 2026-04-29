from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from src.interfaces.api.permissions.is_admin import IsAdmin
from src.interfaces.api.serializers.attendance.attendance_response_serializer import AttendanceResponseSerializer
from src.interfaces.api.serializers.attendance.create_attendance_serializer import CreateAttendanceSerializer
from src.interfaces.api.serializers.attendance.update_attendance_serializer import UpdateAttendanceSerializer
from src.application.use_cases.attendance.create_attendance import CreateAttendanceUseCase
from src.application.use_cases.attendance.delete_attendance import DeleteAttendanceUseCase
from src.application.use_cases.attendance.get_attendance import GetAttendanceUseCase
from src.application.use_cases.attendance.list_attendance import ListAttendanceUseCase
from src.application.use_cases.attendance.update_attendance import UpdateAttendanceUseCase
from src.application.exceptions import NotFoundException, PermissionDeniedException
from src.infrastructure.db.repositories.attendance_repository_impl import DjangoAttendanceRespository
from src.infrastructure.db.repositories.student_repository_impl import DjangoStudentRespository
from src.infrastructure.db.repositories.class_session_repository_impl import DjangoClassSessionRepository

class AttendanceViewSet(ViewSet):
    
    permission_classes = [IsAuthenticated, IsAdmin]
    
    def create(self, request):
        serializer = CreateAttendanceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        use_case = CreateAttendanceUseCase(
            attendance_repo=DjangoAttendanceRespository(),
            student_repo=DjangoStudentRespository(),
            class_session_repo=DjangoClassSessionRepository()
        )
        
        try:
            
            result = use_case.execute(data=serializer.validated_data)
            
            serializer = AttendanceResponseSerializer(result)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        except NotFoundException:
            return Response(
                {
                    "error": {
                        "code": "404_not_found",
                        "message": "Student or class session not found"
                    }
                }, status=status.HTTP_404_NOT_FOUND
            )
    
    def list(self, request):
        use_case = ListAttendanceUseCase(
            attendance_repo=DjangoAttendanceRespository()
        )
        
        attendances = use_case.execute()
        
        serializer = AttendanceResponseSerializer(attendances, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        use_case = GetAttendanceUseCase(
            attendance_repo=DjangoAttendanceRespository()
        )
        
        try:
            
            attendance = use_case.execute(attendance_id=pk)
            
            serializer = AttendanceResponseSerializer(attendance)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except NotFoundException:
            return Response(
                {
                    "error": {
                        "code": "404_not_found",
                        "message": "Attendance not found"
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
        serializer = UpdateAttendanceSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        
        use_case = UpdateAttendanceUseCase(
            attendance_repo=DjangoAttendanceRespository()
        )
        
        try:
            
            attendance = use_case.execute(attendance_id=pk, data=serializer.validated_data, user=request.user)
            
            serializer = AttendanceResponseSerializer(attendance)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except NotFoundException:
            return Response(
                {
                    "error": {
                        "code": "404_not_found",
                        "message": "Attendance not found"
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
        use_case = DeleteAttendanceUseCase(
            attendance_repo=DjangoAttendanceRespository()
        )
        
        try:
            
            use_case.execute(attendance_id=pk, user=request.user)
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        except NotFoundException:
            return Response(
                {
                    "error": {
                        "code": "404_not_found",
                        "message": "Attendance not found"
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