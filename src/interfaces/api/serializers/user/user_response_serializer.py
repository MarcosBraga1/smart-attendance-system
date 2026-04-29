from rest_framework import serializers

class UserResponseSerializer(serializers.Serializer):
    
    id = serializers.IntegerField()
    name = serializers.CharField()
    email = serializers.CharField()