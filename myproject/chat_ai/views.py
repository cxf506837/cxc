from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from ollama import chat

def chat_ai(request):
    if request.method == 'POST':
        user_message = request.POST.get('message', '')
        # 设置退出命令
        if user_message.lower() in ['quit', 'exit']:#lower() 是Python字符串的一个方法，它将字符串中的所有字符转换为小写。这样可以确保无论用户输入的是大写、小写还是混合大小写的命令（如'QUIT'、'Exit'等），都能正确匹配。
            return JsonResponse({'response': '再见！'})#返回一个JSON响应。response是一个字典，其中包含了一个键为'response'的键值对，值为用户输入的消息。
        #配置模型
        stream = chat(
            model='deepseek-r1:1.5b',
            messages=[{'role': 'user', 'content': user_message}],#role: 表示消息的发送者角色。在这里，'user'表示这条消息是由用户发送的
            stream=True#用户可以看到回复是逐步生成的，而不是等待一段时间后突然看到完整的回复。
        )
        #返回响应
        response_content = ""
        for chunk in stream:
            response_content += chunk['message']['content']#message是一个字典，其中包含了一个键为'content'的键值对，值为用户输入的消息。

        return JsonResponse({'response': response_content})#这里的response是返回的响应内容。
    
    return JsonResponse({'response': '欢迎使用聊天程序！'})


'''
如果需要处理用户输入的数据（如表单或 API 请求体），使用 request.POST 或 request.body。
如果需要获取 URL 参数，使用 request.GET。
如果需要获取客户端的元信息（如浏览器类型、认证令牌等），使用 request.headers 或 request.META。
'''

#获取表单参数@
#request.POST.get('message', '')
#request.GET.get('message', '')


#获取请求体的json数据@
#request.body 是HTTP请求的正文部分，它包含用户发送到服务器的数据。
#import json
#json.loads(request.body) 这样就能将request.body转换为Python字典了。
#print(request.body)

#获取请求头
#request.META是一个字典，它包含了关于请求的元数据，如HTTP头、请求方法、请求URL等，相当于request.headers
#request.META['HTTP_USER_AGENT'] 这是一个HTTP头，它包含了用户代理的信息，如浏览器版本、操作系统等。
#request.headers('company') 这是Django提供的一个属性，它包含了请求头信息，包括HTTP头、请求方法、请求URL等。

#request.SEVER_NAME 这是一个服务器名称，它包含了服务器的主机名。@
#request.SERVER_PORT 这是一个服务器端口，它包含了服务器的端口号。@
#request.SERVER_ADDR 这是服务器的ip地址@
#request.SERVER_SOFTWARE 这是一个服务器软件，它包含了服务器的版本信息。@
#request.SERVER_PROTOCOL 这是一个服务器协议，它包含了服务器的协议版本。@


#request.FILES 这是一个包含所有上传文件的字典。只能接受POST请求的数据@@@
#request.POST 这是一个包含所有POST数据的字典。
#request.GET 这是一个包含所有GET数据的字典。
#request.COOKIES 这是一个包含所有COOKIES数据的字典。
#request.META 这是一个包含所有HTTP头信息的字典。
#request.FILES.getlist(key) 这是一个返回所有上传文件的列表。
#request.POST.getlist(key)这是一个返回所有POST数据的列表。

#request.FILES("avatar") 这是个返回一个上传文件。


from django.http import HttpResponse
def my_view(request):
    return HttpResponse("<h1>hello world</h1>")#Django 的 HttpResponse 构造函数允许省略一些参数，因为它们有默认值。例如，content_type 默认为 "text/html"，status 默认为 200


# from django.http import JsonResponse
# def my_view(request):
#     #json数据
#     data=[
#         {"name":"zhangsan"},
#         {"age":18}
#         ]
#     #列表数据
#     data={
#         "name":"zhangsan",
#         "age":18
#     }

#     #return JsonResponse(data) #返回json格式的数据
#     #return JsonResponse(data,safe=False) #列表本身不支持json格式，所以需要safe=False


#返回图片数据
# def my_tupian(request):
#     with open('static/img/1.jpg','rb') as file:
#         data=file.read()
#     return HttpResponse(data,content_type='image/jpeg')

#返回安装包
# def my_zip(request):
#     with open('static/img/1.zip','rb') as file:
#         data=file.read()
#     return HttpResponse(data,content_type='application/zip')

#自定义响应头
# def my_view(request):
#     response=HttpResponse("<h1>hello world</h1>")
#     response['X-Custom-Header']='Custom Value'
#     return response

#跳转/重定向:
# from django.shortcuts import redirect
# def my_view(request):
#     return redirect('https://www.baidu.com/')#myapp:my_view 是一个反向解析的URL，它将返回一个重定向到指定视图的HttpResponse。

#站内跳转
#from django.shortcuts import reverse
# from django.shortcuts import redirect
# def my_view(request):
#     return redirect(reverse('mychat:my_view')) #reverse(namespace:name) namespace是前缀的命名空间，name就是路径别名。

#设置cookie
# from django.http import HttpResponse
# def my_view(request):
#     response=HttpResponse("<h1>hello world</h1>")
#     response.set_cookie('name','zhangsan')#设置cookie
#     return response

#获取cookie
# from django.http import HttpResponse
# def my_view(request):
#     name=request.COOKIES.get('name')#获取cookie
#     response=HttpResponse("<h1>hello world</h1>")
#     response.set_cookie('name','zhangsan')#设置cookie
#     return response

#删除cookie
# from django.http import HttpResponse
# def my_view(request):
#     response=HttpResponse("<h1>hello world</h1>")
#     response.delete_cookie('name')#删除cookie
#     return response

