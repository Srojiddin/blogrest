from rest_framework import viewsets, generics
from apps.categories.models import Categories
from apps.categories.api.serializers import CategorySerializer, CategoryRetrieveSerializer

class CategoryAPIView(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return CategorySerializer
        elif self.action  in ['retrieve']:
            return CategoryRetrieveSerializer
        elif self.action in ['update']:
            return CategorySerializer
        elif self.action == 'destroy':
            return None
        return self.serializer_class

