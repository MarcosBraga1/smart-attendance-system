from django.db import transaction
from src.application.exceptions import PermissionDeniedException

class DeleteAttendanceUseCase:
    
    def __init__(self, attendance_repo):
        self.attendance_repo = attendance_repo
    
    @transaction.atomic
    def execute(self, attendance_id, user):
        
        attendance = self.attendance_repo.get_by_id(attendance_id)
        
        if user.role != "admin":
            raise PermissionDeniedException()
        
        self.attendance_repo.delete(attendance_id)