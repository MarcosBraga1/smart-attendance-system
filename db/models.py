import uuid
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
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
class StudentProfile(models.Model):
    
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name="student_profile")
    registration = models.CharField(max_length=50)
    course = models.CharField(max_length=100)
    
class ProfessorProfile(models.Model):
    
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name="professor_profile")
    department = models.CharField(max_length=100)
    
class Discipline(models.Model):
    
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50)
    semester = models.CharField(max_length=20)
    
    professor = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'professor'},
        related_name='disciplines'
    )
    
class Room(models.Model):
    
    name = models.CharField(max_length=100)
    building = models.CharField(max_length=100)
    
    latitude = models.FloatField()
    longitude = models.FloatField()
    allowed_radius = models.FloatField(help_text="Radius in meters")

class ClassSession(models.Model):
    
    discipline = models.ForeignKey(
        Discipline,
        on_delete=models.CASCADE,
        related_name='sessions'
    )
    
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE
    )
    
    date = models.DateField()
    
    start_time = models.TimeField()
    end_time = models.TimeField()
    
    is_active = models.BooleanField(default=True)
    
    qr_token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    
    class Meta:
        unique_together = ('room', 'date', 'start_time')
    
class Attendance(models.Model):
    
    STATUS_CHOICES = [
        ("present", "Present"),
        ("late", "Late"),
        ("absent", "Absent"),
        ("invalid", "Invalid"),
    ]
    
    student = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'student'},
        related_name='attendances'
    )
    
    class_session = models.ForeignKey(
        ClassSession,
        on_delete=models.CASCADE,
        related_name='attendances'
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    ip_address = models.GenericIPAddressField()
    
    latitude = models.FloatField()
    longitude = models.FloatField()
    
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="absent"
    )
    
    class Meta:
        unique_together = ("student", "class_session")
        indexes = [
            models.Index(fields=["class_session"]),
            models.Index(fields=["student"]),
        ]