from django.urls import path
from . import views

app_name = 'cookie'
urlpatterns = [
    path('cookie/set', views.set_cookie),
    path('cookie/get', views.get_cookie),
    path('cookie/del', views.del_cookie)
]
