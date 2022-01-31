from rest_framework import permissions


class IsBuilder(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        else:
            role = request.user.role.id
            if role == 2:
                return True
            else:
                return False


class IsCreatorFlat(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return obj.creator == request.user


class IsCreatorAnnouncement(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
