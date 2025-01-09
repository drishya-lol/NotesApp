from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey('NoteCategory', on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

class NoteCategory(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name