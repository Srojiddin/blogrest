from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

api_urlpatterns = [
    path('category/', include('apps.categories.api.urls')),
    path('blog/', include('apps.blogs.api.urls'))
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('post', include('apps.blogs.urls'))
]
urlpatterns += api_urlpatterns

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
