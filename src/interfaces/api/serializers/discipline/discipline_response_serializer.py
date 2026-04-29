from rest_framework import serializers
from src.interfaces.api.serializers.user.user_response_serializer import UserResponseSerializer

class DisciplineResponseSerializer(serializers.Serializer):
    
    id = serializers.IntegerField()
    name = serializers.CharField()
    code = serializers.CharField()
    semester = serializers.CharField()
    professor = UserResponseSerializer()