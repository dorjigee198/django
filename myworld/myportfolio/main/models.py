# models.py

from django.db import models

class Experience(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    project_link = models.URLField()

    def __str__(self):
        return self.title


