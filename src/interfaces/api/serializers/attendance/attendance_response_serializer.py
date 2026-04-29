from rest_framework import serializers
from src.interfaces.api.serializers.user.user_response_serializer import UserResponseSerializer
from src.interfaces.api.serializers.class_session.class_session_response_serializer import ClassSessionResponseSerializer

class AttendanceResponseSerializer(serializers.Serializer):
    
    id = serializers.IntegerField()
    student = UserResponseSerializer()
    class_session = ClassSessionResponseSerializer()
    ip_address = serializers.IPAddressField()
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    status = serializers.CharField()