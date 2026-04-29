from rest_framework import serializers

class UpdateRoomSerializer(serializers.Serializer):
    
    name = serializers.CharField()
    building = serializers.CharField()
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    allowed_radius = serializers.FloatField()