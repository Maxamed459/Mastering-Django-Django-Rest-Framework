from rest_framework import permissions

class isStaffEditOrView(permissions.DjangoModelPermissions):

    
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    def has_permission(self, request, view):
        if not request.user.is_staff:
            return False
        return super().has_permission(request, view)

    # def has_permission(self, request, view):
    #     user = request.user
    #     print(user)
    #     if user.is_staff:
    #         if user.has_perm("books.add_book"):
    #             return True
    #         if user.has_perm("books.view_book"):
    #             return True
    #         if user.has_perm("books.change_book"):
    #             return True
    #         if user.has_perm("books.delete_book"):
    #             return True
    #         return False
    #     return False

