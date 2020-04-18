from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('srinu', views.srinu, name='srinu'),
    path('srinu2', views.srinu2, name='srinu2'),
    path('pratyu', views.pratyu, name='pratyu'),
    path('pratyu2', views.pratyu2, name='pratyu2'),
    path('venki', views.venki, name='venki'),
]