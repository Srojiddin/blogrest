from rest_framework import serializers

from apps.blogs.models import Blog, BlogImage


class BlogImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogImage
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    blog_images = BlogImageSerializer(
        read_only=True,
        many=True
    )

    class Meta:
        model = Blog
        fields = '__all__'


class BlogCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = '__all__'



