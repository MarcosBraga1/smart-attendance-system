from src.application.exceptions import NotFoundException
from src.domain.repositories.user_repository import UserRepository
from src.domain.entities.user import User
from db.models import UserModel

class DjangoUserRepository(UserRepository):
    
    def save(self, user):
        obj = UserModel.objects.create(
            email=user.email,
            password=user.password,
            name=user.name,
            role=user.role
        )
        
        return self._to_entity(obj)
        
    def exists_by_email(self, email):
        return UserModel.objects.filter(email=email).exists()
    
    def get_by_email(self, email):
        return UserModel.objects.filter(email=email).first()
    
    def get_by_id(self, user_id):
        try:
            
            user = UserModel.objects.get(id=user_id)
            return self._to_entity(user)
        
        except UserModel.DoesNotExist:
            raise NotFoundException()
        
    def _to_entity(self, model):
        return User(
            id=model.id,
            email=model.email,
            name=model.name,
            role=model.role
        )