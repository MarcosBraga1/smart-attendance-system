from rest_framework import serializers

class UpdateStudentSerializer(serializers.Serializer):
    
    registration = serializers.CharField(required=False)
    course = serializers.CharField(required=False)