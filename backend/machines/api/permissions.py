from rest_framework.permissions import BasePermission

class MachinePermission(BasePermission):
    def has_permission(self, request, view):
        if hasattr(request, "machine") and getattr(request, "machine") != None:
            return True

        return False
