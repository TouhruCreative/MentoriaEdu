from django.urls import path

from .views import ExerciseListCreateView, ExerciseDetailView

urlpatterns = [
    path("exercises/", ExerciseListCreateView.as_view(), name="exercise-list"),
    path("exercises/<int:pk>/", ExerciseDetailView.as_view(), name="exercise-detail"),
]