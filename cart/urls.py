from django.urls import path
from . import views

from .views import (
    cart_summary,
    cart_add,
    cart_delete,
    cart_update
)

app_name='cart'

urlpatterns = [
    path('', cart_summary, name='cart_summary'),
    path('add/', cart_add, name='cart_add'),
    path('delete/', cart_delete, name='cart_delete'),
    path('update/', cart_update, name='cart_update'),
]