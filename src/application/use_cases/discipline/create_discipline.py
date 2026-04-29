from django.db import transaction
from src.domain.entities.discipline import DisciplineModel

class CreateDisciplineUseCase:
    
    def __init__(self, discipline_repo, professor_repo):
        self.discipline_repo = discipline_repo
        self.professor_repo = professor_repo
        
    @transaction.atomic
    def execute(self, data):
        professor = self.professor_repo.get_by_id(data["professor_id"])
        
        discipline = DisciplineModel(
            name=data["name"],
            code=data["code"],
            semester=data["semester"],
            professor=professor
        )
        
        return self.discipline_repo.save(discipline)
        