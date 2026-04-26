class ListStudentsUseCase:
    
    def __init__(self, student_repo):
        self.student_repo = student_repo
        
    def execute(self, user):
        
        if user.role in ["professor", "admin"]:
            return self.student_repo.get_all()
        
        return []