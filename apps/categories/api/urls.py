from rest_framework.routers import DefaultRouter
from apps.categories.api import views
from django.urls import path, include

router = DefaultRouter()
router.register('category', views.CategoryAPIView, basename='category_blog')

urlpatterns = []



urlpatterns += router.urls