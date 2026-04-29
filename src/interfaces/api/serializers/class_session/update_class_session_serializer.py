from rest_framework import serializers

class UpdateClassSessionSerializer(serializers.Serializer):
    
    date = serializers.DateField()
    start_time = serializers.TimeField()
    end_time = serializers.TimeField()
    is_active = serializers.BooleanField()
    
    