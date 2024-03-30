from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

api_urlpatterns = [
    path('', include('apps.comments.api.urls')),
    path('', include('apps.blogs.api.urls'))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.blogs.urls')),
    path('api/', include(api_urlpatterns)),
]
urlpatterns += api_urlpatterns

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
