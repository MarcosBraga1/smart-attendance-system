from src.domain.repositories.student_repository import StudentRepository
from db.models import StudentProfile

class DjangoStudentRespository(StudentRepository):
    
    def save(self, student):
        StudentProfile.objects.create(
            user=student.user,
            registration=student.registration,
            course=student.course
        )