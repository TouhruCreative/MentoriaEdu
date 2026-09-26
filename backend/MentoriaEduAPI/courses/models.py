from django.conf import settings
from django.db import models

class Course(models.Model):
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="courses",
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title} by {self.author}"

class Module(models.Model):
    course =  models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="modules",
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.title} - {self.course}"

class Lesson(models.Model):
    module = models.ForeignKey(
        Module,
        on_delete=models.CASCADE,
        related_name="lessons",
    )
    title = models.CharField(max_length=255) 
    content = models.TextField()
    order = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.title} - {self.module}"