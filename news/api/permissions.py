from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    message = "YOU must be the owner"
    MY_SAFE_METHODS = ['GET', 'PUT']

    def has_permission(self, request, view):
        if request.method in self.MY_SAFE_METHODS:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.from_user == request.user
