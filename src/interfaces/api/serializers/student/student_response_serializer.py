from rest_framework import serializers

class StudentResponseSerializer(serializers.Serializer):
    
    id = serializers.IntegerField()
    name = serializers.CharField(source="user.name")
    email = serializers.EmailField(source="user.email")
    registration = serializers.CharField()
    course = serializers.CharField()