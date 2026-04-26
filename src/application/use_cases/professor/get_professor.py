from src.application.exceptions import PermissionDeniedException

class GetProfessorUseCase:
    
    def __init__(self, professor_repo):
        self.professor_repo = professor_repo
        
    def execute(self, professor_id, user):
        
        professor = self.professor_repo.get_by_id(professor_id)
        
        if user.role != "admin" and professor.user.id != user.id:
            raise PermissionDeniedException()
        
        return professor