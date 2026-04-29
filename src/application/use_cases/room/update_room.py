from src.application.exceptions import PermissionDeniedException

class UpdateRoomUseCase:
    
    def __init__(self, room_repo):
        self.room_repo = room_repo

    def execute(self, room_id, data, user):
        
        room = self.room_repo.get_by_id(room_id)
        
        if user.role != "admin":
            raise PermissionDeniedException()
        
        if "name" in data:
            room.name = data["name"]
            
        if "building" in data:
            room.building = data["building"]
            
        if "latitude" in data:
            room.latitude = data["latitude"]
        
        if "longitude" in data:
            room.longitude = data["longitude"]
            
        if "allowed_radius" in data:
            room.allowed_radius = data["allowed_radius"]
            
        return self.room_repo.update(room)