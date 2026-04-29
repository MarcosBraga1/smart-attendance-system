from src.application.exceptions import NotFoundException
from src.domain.repositories.discipline_repository import DisciplineRepository
from src.domain.entities.discipline import DisciplineModel
from src.domain.entities.user import User
from db.models import Discipline

class DjangoDisciplineRepository(DisciplineRepository):
    
    def get_by_id(self, discipline_id):
        try:
            
            discipline = Discipline.objects.select_related("professor").get(id=discipline_id)
            return self._to_entity(discipline)
        
        except Discipline.DoesNotExist:
            raise NotFoundException()
    
    def save(self, discipline):
        obj = Discipline.objects.create(
            name=discipline.name,
            code=discipline.code,
            semester=discipline.semester,
            professor_id=discipline.professor.id
        )
        
        full_obj = Discipline.objects.select_related("professor").get(id=obj.id)
        
        return self._to_entity(full_obj) 
    
    def update(self, discipline):
        try:
            
            obj = Discipline.objects.get(id=discipline.id)
            
            obj.name = discipline.name
            obj.code = discipline.code
            obj.semester = discipline.semester
            
            obj.save()
            
            return self._to_entity(obj)
        
        except Discipline.DoesNotExist:
            raise NotFoundException()
    
    def delete(self, discipline_id):
        try:
            
            discipline = Discipline.objects.get(id=discipline_id)
            discipline.delete()
            
        except Discipline.DoesNotExist:
            raise NotFoundException()
    
    def get_all(self):
        disciplines = Discipline.objects.select_related("professor").all()
        return [self._to_entity(d) for d in disciplines]
        
    def existis_by_code(self, code):
        return Discipline.objects.filter(code=code).exists()
        
    def _to_entity(self, model):
        return DisciplineModel(
            id=model.id,
            name=model.name,
            code=model.code,
            semester=model.semester,
            professor=self._to_user_entity(model.professor)
        )
        
    def _to_user_entity(self, model):
        return User(
            id=model.id,
            name=model.name,
            email=model.email
        )