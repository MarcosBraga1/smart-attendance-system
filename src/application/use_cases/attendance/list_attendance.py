class ListAttendanceUseCase:
    
    def __init__(self, attendance_repo):
        self.attendance_repo = attendance_repo
        
    def execute(self):
        
        return self.attendance_repo.get_all()