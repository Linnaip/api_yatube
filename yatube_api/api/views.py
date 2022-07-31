from rest_framework import viewsets
from .serializer import PostSerializer
from ..posts.models import Post


class PostViewSet(viewsets.ModelViewsSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
