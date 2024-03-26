from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.blogs.api import views


router = DefaultRouter()
router.register('', views.BlogViewSet, basename="blog_api")

urlpatterns = [
    path('blog/<int:pk>/', views.BlogUpdateDeleteRetrieveAPIView.as_view(), name='blog'),
    path('blog_image/<int:pk>/', views.BlogImageUpdateDeleteRetrieveAPIView.as_view(), name='blog_image'),
    path('blog_image_create/', views.BlogImageCreateAPIView.as_view(), name='blog_image_create'),
]
urlpatterns += router.urls
