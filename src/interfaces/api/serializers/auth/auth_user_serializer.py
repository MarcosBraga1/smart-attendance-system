from rest_framework import serializers
from db.models import UserModel

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
    
        model = UserModel
        fields = ('pk', 'email', 'name', 'role')
        read_only_fields = ('email', 'role')