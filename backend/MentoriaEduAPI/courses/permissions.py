from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsCourseAuthor(BasePermission):
    message = "Вы не являетесь автором этого курса."

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user

class IsModuleAuthor(BasePermission):
    message = "You are not author"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.course.author == request.user


class IsLessonCourseAuthor(BasePermission):
    message = "You are not author"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.module.course.author == request.user