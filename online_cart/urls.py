from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static

from .views import (
    home_view
)

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    #path('', include('store.urls')),
    path('store', include('store.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
