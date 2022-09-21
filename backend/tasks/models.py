from django.db import models
from django.utils import timezone

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=50)
    project = models.CharField(max_length=30)
    date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title
    
    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "project": self.project,
            "date": self.date,

        }