from rest_framework import serializers

class CreateProfessorSerializer(serializers.Serializer):
    
    email = serializers.EmailField()
    password = serializers.CharField()
    name = serializers.CharField()
    department = serializers.CharField()