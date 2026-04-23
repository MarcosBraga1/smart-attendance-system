from src.domain.repositories.professor_repository import ProfessorRepository
from db.models import ProfessorProfile

class DjangoProfessorRepository(ProfessorRepository):
    
    def save(self, professor):
        ProfessorProfile.objects.create(
            user=professor.user,
            department=professor.department
        )