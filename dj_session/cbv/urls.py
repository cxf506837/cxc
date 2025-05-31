# cbv/urls.py
from django.urls import path
from . import views

app_name = 'cbv'  # 添加这行

urlpatterns = [
    path('user/', views.UserView.as_view(), name='user'),
    path('pachong/', views.pachongView.as_view(), name='pachong'),
    path('pachong/biye/', views.BiyeView.as_view(), name='biye'), 
    path('pachong/chong/', views.ChongView.as_view(), name='chong'),
    path('pachong/chaxun/', views.ChaxunView.as_view(), name='chaxun'),
    path('pachong/bijia/', views.BijiaView.as_view(), name='bijia'),  # 确保这个路径存在
]