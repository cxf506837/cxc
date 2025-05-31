from django.urls import path,re_path
from . import views
urlpatterns=[
    path('index',views.index),
    re_path(r"^info/(?P<id>\d+)/$",views.info),
    re_path(r"^info_2/(?P<id>\d+)/(?P<name>\w+)/$",views.info_2),
    path('seckill/', views.SeckillView.as_view(), name='seckill'),
]