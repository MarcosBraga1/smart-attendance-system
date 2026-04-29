from django.db import transaction
from src.application.exceptions import PermissionDeniedException

class DeleteRoomUseCase:
    
    def __init__(self, room_repo):
        self.room_repo = room_repo
        
    @transaction.atomic
    def execute(self, room_id, user):
        
        if user.role != "admin":
            raise PermissionDeniedException()
        
        self.room_repo.delete(room_id)