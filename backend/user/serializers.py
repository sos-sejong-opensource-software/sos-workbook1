from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']


class JWTSignupSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        required=True,
        write_only=True,
        max_length=20
    )

    password = serializers.CharField(
        required=True,
        write_only=True,
        max_length=20,
    )

    class Meta(object):
        model = User
        fields = ['username', 'password']

    def save(self, request):
        user = super().save()

        user.name = self.validated_data['username']
        # AbstractUser 상속받아서 만든 User모델의 경우 set_password()를 사용할 수 있음
        # user.set_password(self.validated_data['password'])
        user.password = self.validated_data['password']
        user.save()

        return user

    def validate(self, data):
        username = data.get('username', None)
        print(User.objects.all())
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError("user already exists")

        return data


class JWTLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True,
        write_only=True,
    )

    password = serializers.CharField(
        required=True,
        write_only=True,
        # style={'input_type': 'password'}
    )

    class Meta(object):
        model = User
        fields = ['username', 'password']

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)

            if user.password != password:
                raise serializers.ValidationError("wrong password")
        else:
            raise serializers.ValidationError("user account not exist")

        token = RefreshToken.for_user(user)
        refresh = str(token)
        access = str(token.access_token)

        data = {
            'user': user,
            'refresh': refresh,
            'access': access,
        }

        return data
