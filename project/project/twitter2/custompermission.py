from rest_framework import permissions


class IsCurrentUserOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.user == request.user


# Edycja profilu użytkownika
class IsCurrentUserOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user
