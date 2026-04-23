from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

class UserModel(AbstractBaseUser, PermissionsMixin):
    
    ROLE_CHOICES = [
        ("student", "Student"),
        ("professor", "Professor"),
        ("admin", "Admin"),
    ]
    
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
class StudentProfile(models.Model):
    
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    registration = models.CharField(max_length=50)
    course = models.CharField(max_length=100)
    
class ProfessorProfile(models.Model):
    
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)