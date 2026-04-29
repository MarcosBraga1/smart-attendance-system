from src.application.exceptions import NotFoundException
from src.domain.repositories.room_repository import RoomRepository
from src.domain.entities.room import RoomModel
from db.models import Room

class DjangoRoomRepository(RoomRepository):
    
    def get_by_id(self, room_id):
        try:
            
            room = Room.objects.get(id=room_id)
            return self._to_entity(room)
        
        except Room.DoesNotExist:
            raise NotFoundException()
    
    def save(self, room):
        obj = Room.objects.create(
            name=room.name,
            building=room.building,
            latitude=room.latitude,
            longitude=room.longitude,
            allowed_radius=room.allowed_radius
        )
        
        return self._to_entity(obj)
    
    def update(self, room):
        try:
            
            obj = Room.objects.get(id=room.id)
            
            obj.name = room.name
            obj.building = room.building
            obj.latitude = room.latitude
            obj.longitude = room.longitude
            obj.allowed_radius = room.allowed_radius
            
            obj.save()
            
            return self._to_entity(obj)
        
        except Room.DoesNotExist:
            raise NotFoundException()
    
    def delete(self, room_id):
        try:
            
            room = Room.objects.get(id=room_id)
            room.detele()
            
        except Room.DoesNotExist:
            raise NotFoundException()
    
    def get_all(self):
        rooms = Room.objects.all()
        return [self._to_entity(r) for r in rooms]
    
    def _to_entity(self, model):
        return RoomModel(
            id=model.id,
            name=model.name,
            building=model.building,
            latitude=model.latitude,
            longitude=model.longitude,
            allowed_radius=model.allowed_radius
        )