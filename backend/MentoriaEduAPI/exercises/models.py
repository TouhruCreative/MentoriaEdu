from django.conf import settings
from django.db import models
from courses.models import Lesson

class Exercise(models.Model):

   lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        related_name="exercises",
    )

   title = models.CharField(max_length=255)
   question = models.TextField()

   TYPE_CHOICES = (
        ("text", "Text"),
        ("code", "Code"),
        ("multiple_choice", "Multiple Choice"),
    )

   type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
   )

   difficulty = models.PositiveIntegerField(
        default=1,
   )

   correct_answer = models.TextField()

   created_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
        return self.title

class Submission(models.Model):
   user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="submissions",
    )

   exercise = models.ForeignKey(
        Exercise,
        on_delete=models.CASCADE,
        related_name="submissions",
    )

   answer = models.TextField()

   is_correct = models.BooleanField(
        null=True,
    )

   score = models.PositiveIntegerField(
        default=0,
    )

   submitted_at = models.DateTimeField(
        auto_now_add=True,
    )

   def __str__(self):
      return f"{self.user} - {self.exercise}"