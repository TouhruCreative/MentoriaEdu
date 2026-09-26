from rest_framework.permissions import BasePermission


class IsCourseAuthor(BasePermission):
    message = "Вы не являетесь автором этого курса."

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user

class IsModuleAuthor(BasePermission):
    message = "You are not author"

    def has_object_permission(self, request, view, obj):
        return obj.course.author == request.user


class IsLessonCourseAuthor(BasePermission):
    message = "You are not author"

    def has_object_permission(self, request, view, obj):
        return obj.module.course.author == request.user