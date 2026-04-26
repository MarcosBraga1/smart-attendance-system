from src.application.exceptions import PermissionDeniedException

class GetStudentUseCase:
    
    def __init__(self, student_repo):
        self.student_repo = student_repo
        
    def execute(self, student_id, user):
        
        student = self.student_repo.get_by_id(student_id)
        
        if user.role == "student" and student.user.id != user.id:
            raise PermissionDeniedException()
        
        return student