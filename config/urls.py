from django.contrib import admin
from django.urls import path,include
from chat.views import main_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", main_view, name="main_view"),
    path('chat/',include('chat.urls',namespace="chat")),
    path('admin/', admin.site.urls),
]

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
