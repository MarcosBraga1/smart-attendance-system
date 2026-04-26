from django.db import transaction
from src.domain.entities.user import User
from src.domain.entities.student import Student
from src.domain.entities.professor import Professor
from src.application.exceptions import AlreadyExistsException

class RegisterUserUseCase:
    
    def __init__(self, user_repo, student_repo, professor_repo, hash_service):
        self.user_repo = user_repo
        self.student_repo = student_repo
        self.professor_repo = professor_repo
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
            role = data["role"]
        )
        
        saved_user = self.user_repo.save(user)
        
        if user.role == "student":
            student = Student(
                user = saved_user,
                registration = data["registration"],
                course = data["course"]
            )
            
            self.student_repo.save(student)
        
        elif user.role == "professor":
            professor = Professor(
                user = saved_user,
                department = data["department"]
            )
            
            self.professor_repo.save(professor)
        
        return {"message": "User created"}