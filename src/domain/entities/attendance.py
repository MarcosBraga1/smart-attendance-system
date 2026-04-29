class AttendanceModel:
    
    def __init__(self, student, class_session, ip_address, latitude, longitude, status, id=None):
        self.id = id
        self.student = student
        self.class_session = class_session
        self.ip_address = ip_address
        self.latitude = latitude
        self.longitude = longitude
        self.status = status