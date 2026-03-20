from django.db import models

class UserModel(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
        