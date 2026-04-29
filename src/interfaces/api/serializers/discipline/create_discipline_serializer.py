from rest_framework import serializers

class CreateDisciplineSerializer(serializers.Serializer):
    
    name = serializers.CharField()
    code = serializers.CharField()
    semester = serializers.CharField()
    professor_id = serializers.IntegerField()