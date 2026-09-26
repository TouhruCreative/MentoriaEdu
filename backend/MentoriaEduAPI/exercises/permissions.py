from rest_framework.permissions import BasePermission


class IsExercisesAuthor(BasePermission):
    message = "Вы не являетесь автором этого курса."

    def has_object_permission(self, request, view, obj):
        return obj.lesson.module.course.author == request.user
