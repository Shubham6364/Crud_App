from django.db import models
import uuid
# Create your models here.
class CrudApp(models.Model):
    Name = models.CharField(max_length=255)
    Email = models.EmailField()
    Address = models.TextField()
    Phone = models.IntegerField()