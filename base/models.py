from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class NoteCategory(models.Model):
    name = models.CharField(max_length=300, unique=True)

class Note(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    category = models.ForeignKey(NoteCategory, on_delete=models.SET_NULL, null=True) # foreign key is one to many relationship
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # date = models.DateTimeField(default=timezone.now)

    # objects  = BaseManager()