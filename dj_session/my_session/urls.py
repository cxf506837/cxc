from django.urls import path
from . import views

urlpatterns = [
    path('get_session', views.get_session ),
    path('set_session', views.set_session ),
    path('del_session', views.del_session ),
]