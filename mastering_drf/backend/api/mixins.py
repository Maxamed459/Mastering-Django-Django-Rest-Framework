from rest_framework import permissions
from .permissions import isStaffEditOrView

class IsStaffOrReadOnlyMixin():
    permission_classes = [permissions.IsAdminUser, isStaffEditOrView]