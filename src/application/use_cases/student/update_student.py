from src.application.exceptions import PermissionDeniedException

class UpdateStudentUseCase:
    
    def __init__(self, student_repo):
        self.student_repo = student_repo
        
    def execute(self, student_id, data, user):
        
        student = self.student_repo.get_by_id(student_id)
        
        if user.role == "student" and student.user.id != user.id:
            raise PermissionDeniedException()
        
        if "registration" in data:
            student.registration = data["registration"]
        
        if "course" in data:
            student.course = data["course"]
        
        updated_user = self.student_repo.update(student)
        
        return updated_user