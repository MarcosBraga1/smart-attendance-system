from rest_framework import serializers

class CreateAttendanceSerializer(serializers.Serializer):
    
    student_id = serializers.IntegerField()
    class_session_id = serializers.IntegerField()
    ip_address = serializers.IPAddressField()
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    status = serializers.ChoiceField(choices=["present", "late", "absent", "invalid"])