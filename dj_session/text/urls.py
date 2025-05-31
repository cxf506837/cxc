from django.urls import path
from .views import my_text

urlpatterns = [
    path('my_text', my_text),
]