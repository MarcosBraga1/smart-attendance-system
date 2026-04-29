from django.db import transaction
from src.application.exceptions import PermissionDeniedException

class DeleteDisciplineUseCase:
    
    def __init__(self, discipline_repo):
        self.discipline_repo = discipline_repo
    
    @transaction.atomic    
    def execute(self, discipline_id, user):
        
        discipline = self.discipline_repo.get_by_id(discipline_id)
        
        if user.role != "admin" and discipline.professor.id != user.id:
            raise PermissionDeniedException()
        
        self.discipline_repo.delete(discipline_id)