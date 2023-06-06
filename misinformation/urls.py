from django.urls import path
from . import views
# from .views import index

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('join/', views.join, name='join'),
]
