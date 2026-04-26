class ListStudentsUseCase:
    
    def __init__(self, student_repo):
        self.student_repo = student_repo
        
    def execute(self, user):
        
        if user.role == "student":
            return self.student_repo.get_by_user_id(user.id)
        
        if user.role in ["professor", "admin"]:
            return self.student_repo.get_all()
        
        return []