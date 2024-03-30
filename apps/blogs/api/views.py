from rest_framework import viewsets, generics

from apps.blogs.api import serializers
from apps.blogs.models import Blog, BlogImage, BlogLike, BlogTag


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = serializers.BlogSerializer

    def get_serializer_class(self):
        if self.action in ['create']:
            return serializers.BlogCreateSerializer
        return self.serializer_class


class BlogImageCreateAPIView(generics.ListCreateAPIView):
    queryset = BlogImage.objects.all()
    serializer_class = serializers.BlogImageSerializer


class BlogUpdateDeleteRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = serializers.BlogSerializer


class BlogImageUpdateDeleteRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogImage.objects.all()
    serializer_class = serializers.BlogImageUpdateRetrieveDestroy


class BlogLikeListCreateAPIView(generics.ListCreateAPIView):
    queryset = BlogLike.objects.all()
    serializer_class = serializers.LikeSerializer


class BlogTagListCreateAPIView(generics.ListCreateAPIView):
    queryset = BlogTag.objects.all()
    serializer_class = serializers.TagSerializer
