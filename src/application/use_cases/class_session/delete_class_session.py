from django.db import transaction
from src.application.exceptions import PermissionDeniedException

class DeleteClassSessionUseCase:
    
    def __init__(self, class_session_repo):
        self.class_session_repo = class_session_repo
        
    @transaction.atomic
    def execute(self, class_session_id, user):
        
        class_session = self.class_session_repo.get_by_id(class_session_id)
        
        if user.role != "admin" and class_session.discipline.professor.id != user.id:
            raise PermissionDeniedException()
        
        self.class_session_repo.delete(class_session_id)