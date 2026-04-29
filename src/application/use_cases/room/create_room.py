from django.db import transaction
from src.domain.entities.room import RoomModel

class CreateRoomUseCase:
    
    def __init__(self, room_repo):
        self.room_repo = room_repo
        
    @transaction.atomic
    def execute(self, data):
        room = RoomModel(
            name=data["name"],
            building=data["building"],
            latitude=data["latitude"],
            longitude=data["longitude"],
            allowed_radius=data["allowed_radius"]
        )
        
        return self.room_repo.save(room)