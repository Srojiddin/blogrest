from rest_framework import serializers

from apps.blogs.models import Blog, BlogImage, BlogLike, BlogTag
from apps.comments.api.serializers import CommentUpdate


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogLike
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogTag
        fields = '__all__'


class BlogImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogImage
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    blog_images = BlogImageSerializer(
        read_only=True,
        many=True
    )

    comment = CommentUpdate(
        read_only=True,
        many=True
    )
    total_likes = serializers.SerializerMethodField()


    class Meta:
        model = Blog
        fields = '__all__'

    def get_total_likes(self,instance):
        return instance.like.all().count()


class BlogCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = '__all__'


class BlogImageUpdateRetrieveDestroy(serializers.ModelSerializer):

    class Meta:
        model = BlogImage
        fields = ['image']




