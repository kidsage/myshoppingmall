from rest_framework.viewsets import ModelViewSet

from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer