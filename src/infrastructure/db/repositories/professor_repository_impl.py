from src.application.exceptions import NotFoundException
from src.domain.repositories.professor_repository import ProfessorRepository
from src.domain.entities.professor import Professor
from db.models import ProfessorProfile

class DjangoProfessorRepository(ProfessorRepository):
    
    def get_by_id(self, professor_id):
        try: 
            
            professor = ProfessorProfile.objects.select_related("user").get(id=professor_id)
            return self._to_entity(professor)
        
        except ProfessorProfile.DoesNotExist:
            raise NotFoundException()
    
    def save(self, professor):
        obj = ProfessorProfile.objects.create(
            user=professor.user,
            department=professor.department
        )
        
        self._to_entity(obj)
        
    def update(self, professor):
        try:
            
            obj = ProfessorProfile.objects.get(id=professor.id)
            
            obj.department = professor.department
            
            obj.save()
            
            return self._to_entity(obj)
        
        except ProfessorProfile.DoesNotExist:
            raise NotFoundException()
    
    def delete(self, professor_id):
        try:
            
            professor = ProfessorProfile.objects.get(id=professor_id)
            professor.delete()
            
        except ProfessorProfile.DoesNotExist:
            raise NotFoundException()
    
    def get_all(self):
        professors = ProfessorProfile.objects.select_related("user").all()
        return [self._to_entity(p) for p in professors]
    
    def _to_entity(self, model):
        return Professor(
            id=model.id,
            user=model.user,
            department=model.department
        )