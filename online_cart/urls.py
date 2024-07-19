from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static

from .views import (
    home_view,
    about,
    login_user,
    logout_user,
    register_user,
    update_user,
    update_password,
)

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('cart', include('cart.urls')),
    path('store', include('store.urls')),
    #path('', include('store.urls')),
    path('about', about, name='about'),
    path('login', login_user, name='login'),
    path('logout', logout_user, name='logout'),
    path('register', register_user, name='register'),
    path('update_user', update_user, name='update_user'),
    path('update_password', update_password, name='update_password'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
