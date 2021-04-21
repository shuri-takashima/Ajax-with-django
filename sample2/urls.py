from django.urls import path
from . import views

app_name ='sample2'
urlpatterns = [
    path('', views.content, name='content'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('comment', views.comment, name='comment'),
]