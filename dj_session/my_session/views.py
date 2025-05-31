from django.shortcuts import render, HttpResponse
# Create your views here.
def set_session(request):
    request.session['name'] = 'zhangsan'
    request.session['age'] = 18
    return HttpResponse('set_session')
def get_session(request):
    # 获取单个 session
    print(request.session.get('age'))
    print(request.session.get('name'))
    # 获取所有 session
    print(dict(request.session.items()))
    return HttpResponse('get_session')

def del_session(request):
    return HttpResponse('del_session')

from django.shortcuts import render, HttpResponse

# Create your views here.

def set_session(request):
    """
    设置session数据。
    将键值对 'name': 'zhangsan' 和 'age': 18 存储到session中。
    """
    request.session['name'] = 'zhangsan'
    request.session['age'] = 18
    return HttpResponse('set_session')

def get_session(request):
    """
    获取session数据。
    打印单个session值（年龄和姓名）以及所有session数据。
    """
    # 获取并打印单个session值
    print(request.session.get('age'))  # 注意：这里应该是get('age')而不是get['age']
    print(request.session.get('name'))
    
    # 获取并打印所有session数据
    print(dict(request.session.items()))
    return HttpResponse('get_session')





def del_session(request):
    """
    删除session数据。
    提供两种删除方式：删除指定名称的session和删除所有session。
    """
    # 删除指定名称的session（例如 "name"）
    if request.session.get("name"):
        request.session.pop("name")
    
    # 删除所有session数据
    request.session.clear()
    return HttpResponse('删除session数据')
