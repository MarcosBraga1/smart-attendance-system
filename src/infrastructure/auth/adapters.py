from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.core.exceptions import ValidationError

class RestrictedSocialAccountAdapter(DefaultSocialAccountAdapter):
    
    def pre_social_login(self, request, sociallogin):
        
        email = sociallogin.user.email
        
        if not email.endswith("@ufvjm.edu.br"):
            raise ValidationError("Access is permitted only for institutional email addresses.")