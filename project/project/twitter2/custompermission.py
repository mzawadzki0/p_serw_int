from rest_framework import permissions


class IsCurrentUserOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user
