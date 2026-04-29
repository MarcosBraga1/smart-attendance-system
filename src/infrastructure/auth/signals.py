from django.db.models.signals import post_save
from django.dispatch import receiver
from db.models import UserModel, StudentProfile, ProfessorProfile

@receiver(post_save, sender=UserModel)
def manage_user_profile(sender, instance, created, **kwargs):
    
    if created:
        if "aluno" in instance.email or instance.email[0].isdigit():
            instance.role = "student"
            StudentProfile.objects.get_or_create(user=instance, registration="GERADO_VIA_SOCIAL")
        else:
            instance.role = "professor"
            ProfessorProfile.objects.get_or_create(user=instance, department="GERAL")
        
        instance.save()