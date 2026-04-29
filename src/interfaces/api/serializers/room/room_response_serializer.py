from rest_framework import serializers

class RoomResponseSerializer(serializers.Serializer):
    
    id = serializers.IntegerField()
    name = serializers.CharField()
    building = serializers.CharField()
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    allowed_radius = serializers.FloatField()