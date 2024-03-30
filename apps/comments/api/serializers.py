from rest_framework import serializers
from apps.comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"

class CommentUpdate(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['text']
