from src.domain.repositories.attendance_repository import AttendanceRepository
from src.domain.entities.attendance import AttendanceModel
from src.domain.entities.class_session import ClassSessionModel
from src.domain.entities.discipline import DisciplineModel
from src.domain.entities.room import RoomModel
from src.domain.entities.user import User
from src.application.exceptions import NotFoundException
from db.models import Attendance

class DjangoAttendanceRespository(AttendanceRepository):
    
    def get_by_id(self, attendance_id):
        try:
            
            attendance = Attendance.objects.select_related('student', 'class_session__room', 'class_session__discipline__professor').get(id=attendance_id)
            return self._to_entity(attendance)
        
        except Attendance.DoesNotExist:
            raise NotFoundException()
    
    def save(self, attendance):
        obj = Attendance.objects.create(
            student_id = attendance.student.id,
            class_session_id = attendance.class_session.id,
            ip_address = attendance.ip_address,
            latitude = attendance.latitude,
            longitude = attendance.longitude,
            status = attendance.status
        )
        
        full_obj = Attendance.objects.select_related('student', 'class_session__room', 'class_session__discipline__professor').get(id=obj.id)
        
        return self._to_entity(full_obj)
    
    def update(self, attendance):
        try:
            
            obj = Attendance.objects.get(id=attendance.id)
            
            obj.ip_address = attendance.ip_address
            obj.latitude = attendance.latitude
            obj.longitude = attendance.longitude
            obj.status = attendance.status
            
            obj.save()
            
            return self._to_entity(obj)
            
        except Attendance.DoesNotExist:
            raise NotFoundException()
    
    def delete(self, attendance_id):
        try:
            
            attendance = Attendance.objects.get(id=attendance_id)
            attendance.delete()
            
        except Attendance.DoesNotExist:
            raise NotFoundException()
    
    def get_all(self):
        attendances = Attendance.objects.select_related('student', 'class_session__room', 'class_session__discipline__professor').all()
        return [self._to_entity(a) for a in attendances]
    
    def _to_entity(self, model):
        return AttendanceModel(
            id=model.id,
            student=self._to_user_entity(model.student),
            class_session=self._to_class_session_entity(model.class_session),
            ip_address=model.ip_address,
            latitude=model.latitude,
            longitude=model.longitude,
            status=model.status
        )
    
    def _to_class_session_entity(self, model):
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