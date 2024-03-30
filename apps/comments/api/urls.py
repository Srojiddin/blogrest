from rest_framework.routers import DefaultRouter
from django.urls import path
from apps.comments.api.views import CommentViewset, CommentUpdateDestroyRetrieveAPIVIew

router = DefaultRouter()
router.register('comment/',CommentViewset,basename='comment')



urlpatterns = [
    path('comments/<int:pk>/',CommentUpdateDestroyRetrieveAPIVIew.as_view(), name='comment_change'),
]
urlpatterns += router.urls