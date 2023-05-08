from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from user.serializers import JWTSignupSerializer, JWTLoginSerializer, UserSerializer


class JWTSignupView(APIView):
    serializer_class = JWTSignupSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=False):
            user = serializer.save(request)

            token = RefreshToken.for_user(user)
            refresh = str(token)
            access = str(token.access_token)
            return Response({'user': UserSerializer(user).data,
                             'access': access,
                             'refresh': refresh}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class JWTLoginView(APIView):
    serializer_class = JWTLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=False):
            user = serializer.validated_data['user']
            access = serializer.validated_data['access']
            refresh = serializer.validated_data['refresh']

            return Response({
                'user': UserSerializer(user).data,
                'access': access,
                'refresh': refresh}, status=status.HTTP_200_OK)

        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
