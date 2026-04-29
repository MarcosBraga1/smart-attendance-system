class ListRoomUseCase:
    
    def __init__(self, room_repo):
        self.room_repo = room_repo
        
    def execute(self):
        
        return self.room_repo.get_all()