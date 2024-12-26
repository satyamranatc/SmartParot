from django.db import models

# Create your models here.
class Subjects(models.Model):
    SubjectName = models.CharField(max_length=100)
    SubjectDesc = models.TextField(max_length=200)
