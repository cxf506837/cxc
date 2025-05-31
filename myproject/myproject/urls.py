from django.contrib import admin
from django.urls import path,include
from chat_ai.views import chat_ai  # 修改: 将导入改为 chat_ai
from mycookie.views import mycookie

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mychat/', include('chat_ai.urls' ,namespace='mychat')),#路由前缀的别名，也叫命名空间
    path('cookie/', include('mycookie.urls'))  # 确认路径配置正确
]