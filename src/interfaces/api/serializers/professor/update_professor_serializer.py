from rest_framework import serializers

class UpdateProfessorSerializer(serializers.Serializer):
    
    department = serializers.CharField(required=False)