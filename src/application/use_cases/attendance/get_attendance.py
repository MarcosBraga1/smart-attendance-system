class GetAttendanceUseCase:
    
    def __init__(self, attendance_repo):
        self.attendance_repo = attendance_repo
        
    def execute(self, attendance_id):
        
        return self.attendance_repo.get_by_id(attendance_id)