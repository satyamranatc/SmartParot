from django.db import models

class Topics(models.Model):
    SubjectId = models.IntegerField()
    TopicName = models.CharField(max_length=100)
    TopicDesc = models.TextField()