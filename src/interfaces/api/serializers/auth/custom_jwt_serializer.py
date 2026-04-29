from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomJWTSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):

        token = super().get_token(user)
        token['role'] = user.role
        token['name'] = user.name
        return token