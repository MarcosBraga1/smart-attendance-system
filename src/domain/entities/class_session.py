class ClassSessionModel:
    
    def __init__(self, discipline, room, date, start_time, end_time, is_active, qr_token, id=None):
        self.id = id
        self.discipline = discipline
        self.room = room
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.is_active = is_active
        self.qr_token = qr_token