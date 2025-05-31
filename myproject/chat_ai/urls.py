from django.urls import path
from . import views

#站内跳转
app_name = 'chat_ai'

urlpatterns = [
    path('my_ai', views.chat_ai),
    path('my_view', views.my_view, name='my_view'),
]
