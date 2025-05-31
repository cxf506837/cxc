# dj_session/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('my_session/', include('my_session.urls')),
    path('text/', include('text.urls')),
    path("tem/", include('tem.urls')),
    path("cbv/", include('cbv.urls', namespace='cbv')),  # 添加命名空间 'cbv'
    path("control/", include('control.urls')),
]