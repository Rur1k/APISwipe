from rest_framework import permissions


class IsBuilder(permissions.BasePermission):
    def has_permission(self, request, view):
        role = request.user.role.id
        if role == 2:
            return True
        else:
            return False
