from django.db import transaction
from src.domain.entities.user import User
from src.domain.entities.student import Student
from src.application.exceptions import AlreadyExistsException

class CreateUserUseCase:
    
    def __init__(self, user_repo, student_repo, hash_service):
        self.user_repo = user_repo
        self.student_repo = student_repo
        self.hash_service = hash_service
        
    @transaction.atomic
    def execute(self, data):
        if self.user_repo.exists_by_email(data["email"]):
            raise AlreadyExistsException()
        
        hashed_password = self.hash_service.hash(data["password"])
        
        user = User(
            email = data["email"],
            password = hashed_password,
            name = data["name"],
            role = "student"
        )
        
        saved_user = self.user_repo.save(user)
        
        student = Student(
            user = saved_user,
            registration = data["registration"],
            course = data["course"]
        )
        
        saved_student = self.student_repo.save(student)
        
        return saved_student