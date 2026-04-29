import uuid
from django.db import transaction
from src.domain.entities.class_session import ClassSessionModel

class CreateClassSessionUseCase:
    
    def __init__(self, class_session_repo, discipline_repo, room_repo):
        self.class_session_repo = class_session_repo
        self.discipline_repo = discipline_repo
        self.room_repo = room_repo
        
    @transaction.atomic
    def execute(self, data):
        discipline = self.discipline_repo.get_by_id(data["discipline_id"])
        room = self.room_repo.get_by_id(data["room_id"])
        
        class_session = ClassSessionModel(
            discipline=discipline,
            room=room,
            date=data["date"],
            start_time=data["start_time"],
            end_time=data["end_time"],
            is_active=True,
            qr_token=uuid.uuid4()
        )
        
        return self.class_session_repo.save(class_session)