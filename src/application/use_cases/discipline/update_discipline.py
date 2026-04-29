from src.application.exceptions import PermissionDeniedException

class UpdateDisciplineUseCase:
    
    def __init__(self, discipline_repo):
        self.discipline_repo = discipline_repo
        
    def execute(self, discipline_id, data, user):
        
        discipline = self.discipline_repo.get_by_id(discipline_id)
        
        if user.role != "admin" and discipline.professor.id != user.id:
            raise PermissionDeniedException()
        
        if "name" in data:
            discipline.name = data["name"]
            
        if "code" in data:
            discipline.code = data["code"]
            
        if "semester" in data:
            discipline.semester = data["semester"]
            
        return self.discipline_repo.update(discipline)