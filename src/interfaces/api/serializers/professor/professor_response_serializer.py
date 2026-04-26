from rest_framework import serializers

class ProfessorResponseSerializer(serializers.Serializer):
    
    id = serializers.IntegerField()
    name = serializers.CharField(source="user.name")
    email = serializers.EmailField(source="user.email")
    department = serializers.CharField()