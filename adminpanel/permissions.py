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


class IsCreaterFlat(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print(obj)
        return request.user == obj
