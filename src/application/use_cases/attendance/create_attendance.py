from django.db import transaction
from src.domain.entities.attendance import AttendanceModel

class CreateAttendanceUseCase:
    
    def __init__(self, attendance_repo, student_repo, class_session_repo):
        self.attendance_repo = attendance_repo
        self.student_repo = student_repo
        self.class_session_repo = class_session_repo
        
    @transaction.atomic
    def execute(self, data):
        student = self.student_repo.get_by_id(data["student_id"])
        class_session = self.class_session_repo.get_by_id(data["class_session_id"])
        
        attendance = AttendanceModel(
            student=student,
            class_session=class_session,
            ip_address=data["ip_address"],
            latitude=data["latitude"],
            longitude=data["longitude"],
            status=data["status"]
        )
        
        return self.attendance_repo.save(attendance)