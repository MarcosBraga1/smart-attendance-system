from src.domain.repositories.class_session import ClassSessionRepository
from src.application.exceptions import NotFoundException
from src.domain.entities.class_session import ClassSessionModel
from src.domain.entities.room import RoomModel
from src.domain.entities.discipline import DisciplineModel
from src.domain.entities.user import User
from db.models import ClassSession

class DjangoClassSessionRepository(ClassSessionRepository):
    
    def get_by_id(self, class_session_id):
        try:
            
            class_session = ClassSession.objects.select_related("discipline__professor", "room").get(id=class_session_id)
            return self._to_entity(class_session)
        
        except ClassSession.DoesNotExist:
            raise NotFoundException()
    
    def save(self, class_session):
        obj = ClassSession.objects.create(
            discipline_id=class_session.discipline.id,
            room_id=class_session.room.id,
            date=class_session.date,
            start_time=class_session.start_time,
            end_time=class_session.end_time,
            qr_token=class_session.qr_token
        )
        
        full_obj = ClassSession.objects.select_related("discipline__professor", "room").get(id=obj.id)
        
        return self._to_entity(full_obj)
    
    def update(self, class_session):
        try:
            
            obj = ClassSession.objects.get(id=class_session.id)
            
            obj.date = class_session.date
            obj.start_time = class_session.start_time
            obj.end_time = class_session.end_time
            obj.is_active = class_session.is_active
            
            obj.save()
            
            return self._to_entity(obj)
            
        except ClassSession.DoesNotExist:
            raise NotFoundException()
    
    def delete(self, class_session_id):
        try:
            
            class_session = ClassSession.objects.get(id=class_session_id)
            class_session.delete()
            
        except ClassSession.DoesNotExist:
            raise NotFoundException()
    
    def get_all(self):
        class_sessions = ClassSession.objects.select_related("discipline__professor", "room").all()
        return [self._to_entity(cs) for cs in class_sessions]
    
    def _to_entity(self, model):
        return ClassSessionModel(
            id=model.id,
            discipline=self._to_discipline_entity(model.discipline),
            room=self._to_room_entity(model.room),
            date=model.date,
            start_time=model.start_time,
            end_time=model.end_time,
            is_active=model.is_active,
            qr_token=model.qr_token
        )
    
    def _to_discipline_entity(self, model):
        return DisciplineModel(
            id=model.id,
            name=model.name,
            code=model.code,
            semester=model.semester,
            professor=self._to_user_entity(model.professor)
        )
    
    def _to_room_entity(self, model):
        return RoomModel(
            id=model.id,
            name=model.name,
            building=model.building,
            latitude=model.latitude,
            longitude=model.longitude,
            allowed_radius=model.allowed_radius
        )
    
    def _to_user_entity(self, model):
        return User(
            id=model.id,
            name=model.name,
            email=model.email
        )