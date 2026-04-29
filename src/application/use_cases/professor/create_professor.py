from django.db import transaction
from src.domain.entities.user import User
from src.domain.entities.professor import Professor
from src.application.exceptions import AlreadyExistsException

class CreateProfessorUseCase:
    
    def __init__(self, user_repo, professor_repo, hash_service):
        self.user_repo = user_repo
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
            role = "professor"
        )
        
        saved_user = self.user_repo.save(user)
        
        professor = Professor(
            user = saved_user,
            department= data["department"]
        )
        
        saved_professor = self.professor_repo.save(professor)
        
        return saved_professor