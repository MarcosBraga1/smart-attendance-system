from rest_framework import serializers

class CreateClassSessionSerializer(serializers.Serializer):
    
    discipline_id = serializers.IntegerField()
    room_id = serializers.IntegerField()
    date = serializers.DateField()
    start_time = serializers.TimeField()
    end_time = serializers.TimeField()
    is_active = serializers.BooleanField()
    