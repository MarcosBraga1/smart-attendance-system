from rest_framework import serializers

class UpdateAttendanceSerializer(serializers.Serializer):
    
    ip_address = serializers.IPAddressField()
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    status = serializers.ChoiceField(choices=["present", "late", "absent", "invalid"])