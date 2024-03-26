from rest_framework import viewsets, generics

from apps.categories.models import Categories
from apps.blogs.api.serializers import BlogSerializer
from rest_framework import serializers



class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = '__all__'


class CategoryRetrieveSerializer(serializers.ModelSerializer):
    category = BlogSerializer(
        read_only=True,
        many=True,
    )

    class Meta:
        model = Categories
        fields = '__all__'
