from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.blogs.api import views


router = DefaultRouter()
router.register('blog/', views.BlogViewSet, basename="blog_api")

urlpatterns = [
    path('blog/<int:pk>/', views.BlogUpdateDeleteRetrieveAPIView.as_view(), name='blog'),
    path('image/<int:pk>/', views.BlogImageUpdateDeleteRetrieveAPIView.as_view(), name='blog_image'),
    path('images/', views.BlogImageCreateAPIView.as_view(), name='blog_image_create'),
    path('like/',views.BlogLikeListCreateAPIView.as_view(), name='blog_like'),
    path('tag/',views.BlogTagListCreateAPIView.as_view(), name='blog_tag')
]
urlpatterns += router.urls
