from src.application.exceptions import NotFoundException
from src.domain.repositories.student_repository import StudentRepository
from src.domain.entities.student import Student
from db.models import StudentProfile

class DjangoStudentRespository(StudentRepository):
    
    def get_by_id(self, student_id):
        try:
            
            student = StudentProfile.objects.select_related("user").get(id=student_id)
            return self._to_entity(student)
        
        except StudentProfile.DoesNotExist:
            raise NotFoundException()
    
    def save(self, student):
        StudentProfile.objects.create(
            user=student.user,
            registration=student.registration,
            course=student.course
        )
        
    def update(self, student):
        try:
            
            obj = StudentProfile.objects.get(id=student.id)
            
            obj.registration = student.registration
            obj.course = student.course
            
            obj.save()
            
            return self._to_entity(obj)
        
        except StudentProfile.DoesNotExist:
            raise NotFoundException()
    
    def delete(self, student_id):
        try:
            
            student = StudentProfile.objects.get(id=student_id)
            student.delete()
        
        except StudentProfile.DoesNotExist:
            raise NotFoundException()
    
    def get_all(self):
        students = StudentProfile.objects.select_related("user").all()
        return [self._to_entity(s) for s in students]
    
    def _to_entity(self, model):
        return Student(
            id=model.id,
            user=model.user,
            registration=model.registration,
            course=model.course
        )