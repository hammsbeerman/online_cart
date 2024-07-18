from django.urls import path
from . import views

from .views import (
    product,
    category,
)

app_name='store'

urlpatterns = [
    path('product/<int:pk>', product, name='product'),
    path('category/<str:cat>', category, name='category'),
    #path('category_summary/', category_summary, name='category_summary'),
]
