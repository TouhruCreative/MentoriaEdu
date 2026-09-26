
from rest_framework import serializers

from .models import Exercise, Submission


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = [
            "id",
            "lesson",
            "title",
            "question",
            "type",
            "difficulty",
            "correct_answer",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
        ]


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = [
            "id",
            "user",
            "exercise",
            "answer",
            "is_correct",
            "score",
            "submitted_at",
        ]
        read_only_fields = [
            "id",
            "user",
            "is_correct",
            "score",
            "submitted_at",
        ]

