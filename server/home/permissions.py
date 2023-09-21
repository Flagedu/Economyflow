from rest_framework import permissions


class LeadsPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.username == "marketing66"