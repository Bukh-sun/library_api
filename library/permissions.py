from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Чтение (GET, HEAD, OPTIONS) — разрешен всем
        if request.method in permissions.SAFE_METHODS:
            return True
        # Изменение/удаление — только если пользователь = владелец книги
        return obj.added_by == request.user