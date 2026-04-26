from django.db import transaction
from src.application.exceptions import PermissionDeniedException

class DeleteProfessorUseCase:
    
    def __init__(self, professor_repo):
        self.professor_repo = professor_repo
    
    @transaction.atomic
    def execute(self, professor_id, user):
        
        professor = self.professor_repo.get_by_id(professor_id)
        
        if user.role != "admin" and professor.user.id != user.id:
            raise PermissionDeniedException()
        
        self.professor_repo.delete(professor_id)