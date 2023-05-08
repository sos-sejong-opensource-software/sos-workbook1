import jwt
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from djangoreactapi.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer, PostDetailSerializer


class ListPostView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    # 00-01 post 생성
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer

    # 00-00 post 리스트 전체 조회
    def list(self, request):
        queryset = self.get_queryset()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data, status=HTTP_200_OK)



class DetailPostView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    # 00-02 post 상세 조회
    def get(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        serializer = PostDetailSerializer(post)
        return Response(serializer.data, status=HTTP_200_OK)

    # 00-03 post 수정
    def put(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        serializer = PostDetailSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            updated_post = serializer.save()
            serializer = PostDetailSerializer(updated_post)
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # 토큰을 받아서 user인증하는 방법 구현중
        token = request.GET('token')
        print(token)
        # payload = jwt.decode(token,)
        post = get_object_or_404(Post, id=pk)
        post.delete()
        # serializer = PostSerializer(post)
