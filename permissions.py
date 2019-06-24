from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    #Read permissions are allowed to any request
    #So we will always allow GET, HEAD or OPTIONS requests
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: #checks whether it is only GET or among few others
            return True                                

        #instance must have an attribute named 'owner'
        return obj.owner == request.user  