from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class IsOwnerForPrivate(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.is_public:
            return True
        return obj.owner == request.user


class PublicReadAccess(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.is_public


class PrivateOwnerAccess(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
