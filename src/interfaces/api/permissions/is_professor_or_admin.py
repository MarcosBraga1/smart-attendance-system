from rest_framework.permissions import BasePermission

class IsProfessorOrAdmin(BasePermission):
    
    def has_permission(self, request, view):
        return request.user.role in ["professor", "admin"]