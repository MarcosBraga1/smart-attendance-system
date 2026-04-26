from rest_framework.permissions import BasePermission

class IsStudentOrAdmin(BasePermission):
    
    def has_permission(self, request, view):
        return request.user.role in ["student", "admin"]