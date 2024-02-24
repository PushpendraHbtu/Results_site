from django.db import models

# Create your models here.

class faculty_login(models.Model):
    fuser=models.CharField(max_length=100)
    fpass=models.CharField(max_length=100)
    
    def __str__(self):
        return self.fuser