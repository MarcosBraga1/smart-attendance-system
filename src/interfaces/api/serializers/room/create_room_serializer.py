from rest_framework import serializers

class CreateRoomSerializer(serializers.Serializer):
    
    name = serializers.CharField()
    building = serializers.CharField()
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    allowed_radius = serializers.FloatField()