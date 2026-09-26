from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .models import Course, Module, Lesson
from .serializers import CourseSerializer, ModuleSerializer, LessonSerializer
from .permissions import IsCourseAuthor, IsModuleAuthor, IsLessonCourseAuthor


class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [
        IsAuthenticated,
        IsCourseAuthor,
    ]




class ModuleListCreateView(generics.ListCreateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def perform_create(self, serializer):
        course = serializer.validated_data["course"]
        if course.author != self.request.user:
            raise PermissionDenied("You are not the course author")
        serializer.save()

class ModuleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [
        IsAuthenticated,
        IsModuleAuthor,
    ]



class LessonListCreateView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def perform_create(self, serializer):
        module = serializer.validated_data["module"]
        if module.course.author != self.request.user:
            raise PermissionDenied("You are not the course author")
        serializer.save()

class LessonDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [
        IsAuthenticated,
        IsLessonCourseAuthor,
    ]