import bcrypt
from src.domain.services.hash_service import HashService

class BcryptHashService(HashService):
    
    def hash(self, value: str) -> str:
        return bcrypt.hashpw(value.encode(), bcrypt.gensalt()).decode()
    
    def verify(self, value, hashed):
        return bcrypt.checkpw(value.encode(), hashed.encode())
