from rest_framework import serializers
from src.interfaces.api.serializers.discipline.discipline_response_serializer import DisciplineResponseSerializer
from src.interfaces.api.serializers.room.room_response_serializer import RoomResponseSerializer

class ClassSessionResponseSerializer(serializers.Serializer):
    
    id = serializers.IntegerField()
    date = serializers.DateField()
    start_time = serializers.TimeField()
    end_time = serializers.TimeField()
    is_active = serializers.BooleanField()
    qr_token = serializers.CharField()
    discipline = DisciplineResponseSerializer()
    room = RoomResponseSerializer()