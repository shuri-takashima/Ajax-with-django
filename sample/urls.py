from django.urls import path
from . import views

urlpatterns = [
    path('', views.article, name='articles'),
    path('like', views.like, name='like'),
]
