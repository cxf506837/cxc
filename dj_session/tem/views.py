# views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import os

def index(request):
    from django.template.loader import get_template

    # 缓存文件路径
    cache_path = settings.BASE_DIR / "cache" / "index.html"

    # 删除缓存文件
    if os.path.exists(cache_path):
        print("删除缓存页面")
        os.remove(cache_path)#remove方法用于删除文件或目录，如果文件或目录不存在，则会抛出FileNotFoundError异常

    # 获取模板
    template = get_template('index.html')

    # 渲染模板
    name = 'zhangsan'
    age = 18
    num = [1, 2, 3, 4, 5]
    filesize = 3276822
    address = ["深圳市", '南山区', '深职院']
    my_content = "我的个人主页,https://www.baidu.com"
    my_mobile_num = '13410923843'
    content = template.render(locals(), request)#render方法返回一个字符串，这个字符串就是渲染后的HTML代码
    print("渲染内容:", content)  # 添加调试信息

    # 缓存页面
    with open(cache_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return HttpResponse(content) 

        
