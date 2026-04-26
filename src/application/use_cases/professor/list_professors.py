class ListProfessorsUseCase:
    
    def __init__(self, professor_repo):
        self.professor_repo = professor_repo
        
    def execute(self, user):
        
        return self.professor_repo.get_all()