from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):
    message = "Доступ разрешён только модераторам."

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == "moderator"
        )


class IsOwner(BasePermission):
    message = "Вы можете работать только со своим аккаунтом."

    def has_object_permission(self, request, view, obj):
        return obj == request.user