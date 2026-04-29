from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from src.interfaces.api.permissions.is_professor_or_admin import IsProfessorOrAdmin
from src.interfaces.api.serializers.student.create_student_serializer import CreateStudentSerializer
from src.interfaces.api.serializers.student.student_response_serializer import StudentResponseSerializer
from src.interfaces.api.serializers.student.update_student_serializer import UpdateStudentSerializer
from src.application.use_cases.student.create_student import CreateUserUseCase
from src.application.use_cases.student.list_students import ListStudentsUseCase
from src.application.use_cases.student.get_student import GetStudentUseCase
from src.application.use_cases.student.update_student import UpdateStudentUseCase
from src.application.use_cases.student.delete_student import DeleteStudentUseCase
from src.application.exceptions import AlreadyExistsException, NotFoundException, PermissionDeniedException
from src.infrastructure.db.repositories.user_repository_impl import DjangoUserRepository
from src.infrastructure.db.repositories.student_repository_impl import DjangoStudentRespository
from src.infrastructure.auth.hash_service_impl import BcryptHashService

class StudentViewSet(ViewSet):
    
    permission_classes = [IsAuthenticated, IsProfessorOrAdmin]

    def create(self, request):
        serializer = CreateStudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        use_case = CreateUserUseCase(
            user_repo=DjangoUserRepository(),
            student_repo=DjangoStudentRespository(),
            hash_service=BcryptHashService()
        )
        
        try:
            
            result = use_case.execute(data=serializer.validated_data)
            
            serializer = StudentResponseSerializer(result)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        except AlreadyExistsException as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        use_case = ListStudentsUseCase(
            student_repo=DjangoStudentRespository()
        )
        
        students = use_case.execute(user=request.user)
        
        serializer = StudentResponseSerializer(students, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        use_case = GetStudentUseCase(
            student_repo=DjangoStudentRespository()
        )
        
        try:
            
            student = use_case.execute(student_id=pk, user=request.user)
            
            serializer = StudentResponseSerializer(student)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except NotFoundException:
            return Response(
                {
                    "error": {
                        "code": "404_not_found",
                        "message": "Student not found"
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
        serializer = UpdateStudentSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        
        use_case = UpdateStudentUseCase(
            student_repo=DjangoStudentRespository()
        )
        
        try:
            
            student = use_case.execute(student_id=pk, data=serializer.validated_data, user=request.user)
            
            serializer = StudentResponseSerializer(student)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except NotFoundException:
            return Response(
                {
                    "error": {
                        "code": "404_not_found",
                        "message": "Student not found"
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
        use_case = DeleteStudentUseCase(
            student_repo=DjangoStudentRespository()
        )
        
        try:
            
            use_case.execute(student_id=pk, user=request.user)
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        except NotFoundException:
            return Response(
                {
                    "error": {
                        "code": "404_not_found",
                        "message": "Student not found"
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