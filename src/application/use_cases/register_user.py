from src.domain.entities.user import User
from src.application.exceptions import AlreadyExistsException

class RegisterUserUseCase:
    def __init__(self, user_repo, hash_service):
        self.user_repo = user_repo
        self.hash_service = hash_service
    
    def execute(self, data):
        if self.user_repo.exists_by_email(data["email"]):
            raise AlreadyExistsException()
        
        hashed_password = self.hash_service.hash(data["password"])
        
        user = User(
            email = data["email"],
            password = hashed_password
        )
        
        self.user_repo.save(user)
        
        return {"message": "User created"}