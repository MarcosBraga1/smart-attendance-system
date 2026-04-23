from rest_framework import serializers

class RegisterSerializer(serializers.Serializer):
    
    email = serializers.EmailField()
    password = serializers.CharField()
    name = serializers.CharField()
    role = serializers.ChoiceField(choices=["student", "professor", "admin"])
    
    registration = serializers.CharField(required=False)
    course = serializers.CharField(required=False)
    department = serializers.CharField(required=False)
    
    def validate(self, data):
        role = data.get("role")
        
        if role == "student":
            if not data.get("registration"):
                raise serializers.ValidationError({
                    "registration": "This field is required for students"
                })
                
            if not data.get("course"):
                raise serializers.ValidationError({
                    "course": "This field is required for students"
                })
        
        if role == "professor":
            if not data.get("department"):
                raise serializers.ValidationError({
                    "department": "This field is required for professors"
                })
        
        return data