from rest_framework import serializers

class UpdateDisciplineSerializer(serializers.Serializer):
    
    name = serializers.CharField()
    code = serializers.CharField()
    semester = serializers.CharField()
    