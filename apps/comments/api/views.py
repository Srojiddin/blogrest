from rest_framework import generics, viewsets

from apps.comments.models import Comment
from apps.comments.api.serializers import CommentSerializer, CommentUpdate


class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


    def get_serializer_class(self):
        if self.action in ['create']:
            return self.serializer_class
        return self.serializer_class


class CommentUpdateDestroyRetrieveAPIVIew(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentUpdate
