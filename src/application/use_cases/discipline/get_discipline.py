class GetDisciplineUseCase:
    
    def __init__(self, discipline_repo):
        self.discipline_repo = discipline_repo
        
    def execute(self, discipline_id):
        
        return self.discipline_repo.get_by_id(discipline_id)