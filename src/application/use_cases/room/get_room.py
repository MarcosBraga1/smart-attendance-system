from src.application.exceptions import PermissionDeniedException

class GetRoomUseCase:
    
    def __init__(self, room_repo):
        self.room_repo = room_repo
        
    def execute(self, room_id, user):
        
        if user.role != "admin":
            raise PermissionDeniedException()
        
        return self.room_repo.get_by_id(room_id)