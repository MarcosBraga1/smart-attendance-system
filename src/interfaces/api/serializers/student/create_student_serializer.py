from rest_framework import serializers

class CreateStudentSerializer(serializers.Serializer):
    
    email = serializers.EmailField()
    password = serializers.CharField()
    name = serializers.CharField()
    registration = serializers.CharField()
    course = serializers.CharField()