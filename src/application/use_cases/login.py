from src.application.exceptions import InvalidCredentialsException

class LoginUseCase:
    
    def __init__(self, user_repo, hash_service, jwt_service):
        self.user_repo = user_repo
        self.hash_service = hash_service
        self.jwt_service = jwt_service
    
    def execute(self, data):
        user = self.user_repo.get_by_email(data["email"])
            
        if not user or not self.hash_service.verify(data["password"], user.password):
            raise InvalidCredentialsException()
        
        tokens = self.jwt_service.generate_token(user)
        
        return {
            "message": "User authenticated",
            "user": {
                "id": user.id,
                "email": user.email,
                "name": user.name,
                "role": user.role
            },
            **tokens
        }
            