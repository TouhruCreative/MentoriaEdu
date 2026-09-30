from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsExercisesAuthor(BasePermission):
    message = "Вы не являетесь автором этого курса."

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.lesson.module.course.author == request.user
