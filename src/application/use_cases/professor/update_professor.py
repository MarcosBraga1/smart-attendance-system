from src.application.exceptions import PermissionDeniedException

class UpdateProfessorUseCase:
    
    def __init__(self, professor_repo):
        self.professor_repo = professor_repo
        
    def execute(self, professor_id, data, user):
        
        professor = self.professor_repo.get_by_id(professor_id)
        
        if user.role != "admin" and professor.user.id != user.id:
            raise PermissionDeniedException()
        
        if "department" in data:
            professor.department = data["department"]
        
        updated_professor = self.professor_repo.update(professor)
        
        return updated_professor