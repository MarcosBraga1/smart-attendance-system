from src.application.exceptions import PermissionDeniedException

class UpdateClassSessionUseCase:
    
    def __init__(self, class_session_repo):
        self.class_session_repo = class_session_repo
        
    def execute(self, class_session_id, data, user):
        
        class_session = self.class_session_repo.get_by_id(class_session_id)
        
        if user.role != "admin" and class_session.discipline.professor.id != user.id:
            raise PermissionDeniedException()
        
        if "date" in data:
            class_session.date = data["date"]
        
        if "start_time" in data:
            class_session.start_time = data["start_time"]
            
        if "end_time" in data:
            class_session.end_time = data["end_time"]
            
        if "is_active" in data:
            class_session.is_active = data["is_active"]
            
        return self.class_session_repo.update(class_session)