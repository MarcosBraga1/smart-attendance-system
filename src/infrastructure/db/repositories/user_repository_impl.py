from src.domain.repositories.user_repository import UserRepository
from db.models import UserModel

class DjangoUserRepository(UserRepository):
    def save(self, user):
        UserModel.objects.create(
            email=user.email,
            password=user.password
        )
        
    def exists_by_email(self, email):
        return UserModel.objects.filter(email=email).exists()