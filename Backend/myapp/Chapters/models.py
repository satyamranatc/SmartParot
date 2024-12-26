from django.db import models

class Chapters(models.Model):
    TopicId = models.IntegerField()
    ChapterName = models.CharField(max_length=100)
    ChapterDesc = models.TextField()