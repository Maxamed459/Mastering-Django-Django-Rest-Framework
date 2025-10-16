# books/permissions.py
from rest_framework import permissions

class IsOwnerOrReadOnlyOnly(permissions.BasePermission):
    """
    Only the owner of the object can edit or delete it.
    Everyone else can only read.
    """
    def has_permission(self, request, view):
        #GET, HEAD, OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True
        # only authenticated users can create product and edit and delete theirs
        return request.user and request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # only if the user is the owner of the product can edit and delete
        return obj.owner == request.user
