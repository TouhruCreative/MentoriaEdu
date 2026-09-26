from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .models import Exercise, Submission
from .serializers import SubmissionSerializer, ExerciseSerializer
from .permissions import IsExercisesAuthor

class ExerciseListCreateView(generics.ListCreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        lesson = serializer.validated_data["lesson"]
        if lesson.module.course.author != self.request.user:
            raise PermissionDenied("You are not the course author")
        serializer.save()


class ExerciseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [
        IsAuthenticated,
        IsExercisesAuthor
    ]