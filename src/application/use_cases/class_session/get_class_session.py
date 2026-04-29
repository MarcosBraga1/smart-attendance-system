class GetClassSessionUseCase:
    
    def __init__(self, class_session_repo):
        self.class_session_repo = class_session_repo
        
    def execute(self, class_session_id):
        
        return self.class_session_repo.get_by_id(class_session_id)