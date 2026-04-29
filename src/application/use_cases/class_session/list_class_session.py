class ListClassSessionUseCase:
    
    def __init__(self, class_session_repo):
        self.class_session_repo = class_session_repo
        
    def execute(self):
        
        return self.class_session_repo.get_all()