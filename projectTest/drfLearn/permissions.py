from rest_framework import permissions


class CustomerPermission(permissions.BasePermission):
    message = "You have not Permissions to do this"

    def has_permission(self, request, view):
        pass

    def has_object_permission(self, request, view, obj):
        pass


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
