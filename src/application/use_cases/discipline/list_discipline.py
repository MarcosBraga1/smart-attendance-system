class ListDisciplineUseCase:
    
    def __init__(self, discipline_repo):
        self.discipline_repo = discipline_repo
        
    def execute(self):
        
        return self.discipline_repo.get_all()