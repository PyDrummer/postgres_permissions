from rest_framework import permissions
import rest_framework

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if obj.author is None: # replace author with the ForeignKey in models
            return True
        
        return obj.author == request.user