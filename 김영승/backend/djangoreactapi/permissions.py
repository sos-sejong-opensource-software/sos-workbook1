import jwt
from rest_framework import permissions
import rest_framework_simplejwt

from user.models import User


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # 읽기 권한 요청일 경우 허용
        if request.method in permissions.SAFE_METHODS:
            return True
        header_token = request.META.get('HTTP_AUTHORIZATION', None)
        token = header_token.split(' ')
        payload = jwt.decode(token, "secret", algorithms=["HS256"])
        username = User.objects.filter(user_id=payload['user_id']).get('username')
        # 요청자(request.user)가 객체(Post)의 created_user 와 동일한지 확인
        return obj.created_user == username
