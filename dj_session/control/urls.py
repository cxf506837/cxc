# control/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('seckill/', views.SeckillView.as_view(), name='seckill'),
]