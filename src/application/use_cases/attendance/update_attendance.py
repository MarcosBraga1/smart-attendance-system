from src.application.exceptions import PermissionDeniedException

class UpdateAttendanceUseCase:
    
    def __init__(self, attendance_repo):
        self.attendance_repo = attendance_repo
        
    def execute(self, attendance_id, data, user):
        
        attendance = self.attendance_repo.get_by_id(attendance_id)
            
        if user.role != "admin":
            raise PermissionDeniedException()
        
        if "ip_address" in data:
            attendance.ip_address = data["ip_address"]
            
        if "latitude" in data:
            attendance.latitude = data["latitude"]
            
        if "longitude" in data:
            attendance.longitude = data["longitude"]
            
        if "status" in data:
            attendance.status = data["status"]
            
        return self.attendance_repo.update(attendance)