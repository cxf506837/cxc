def simple_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print("1. 请求到达中间件之前")
        print(request.headers)  # 判断用户身份，从请求头中获取 jwt token
        print(request.META.get('REMOTE_ADDR'), request.path)  # 记录用户的访问历史和访问来源

        response = get_response(request)  # response 是视图函数返回的响应对象，也就是 HttpResponse对象

        print("6. 响应返回中间件之后")
        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware


from django.utils.deprecation import MiddlewareMixin

class my_middleware(MiddlewareMixin):
    def process_request(self, request):    #重点1
        # 方法名是固定的，会在请求之后，进入视图函数之前被调用
        # 用途，权限，路由分发，cdr,用户身份识别，黑名单，白名单。
        print("2. 请求到达视图函数之前")
        print(request.headers)  # 判断用户身份，从请求头中获取 jwt token
        print(request.META.get('REMOTE_ADDR'), request.path)  # 记录用户的访问历史和访问来源

    def process_view(self, request, view_func, view_args, view_kwargs):
        # 用途：识别参数，根据参数判断否缓存，返回缓存数据还是执行视图函数。
        print("3. 视图函数执行之前，参数接收之后")

    def process_response(self, request, response):   #重点2
        # 视图函数执行之后，返回response对象之前被调用
        # 用途：记录操作历史，访问历史
        # 注意：
        # 当前方法可以返回response对象，但如果返回response对象，则不会执行视图函数，直接返回response对象。
        # 也可以不返回response对象，则django会自动继续执行视图函数。
        print("4. 视图函数执行之后，响应返回之前")
        return response  # 一定要返回，则不会执行视图函数，直接返回response对象，导致报错

    def process_exception(self, request, exception):
        # 视图函数执行过程中，如果出现异常，则被调用
        # 用途：记录异常，异常日志，异常处理
        print("5. 视图函数执行过程中出现异常")

    def process_template_response(self, request, response):
        # 视图函数执行过程中，如果返回的是 TemplateResponse 对象，则被调用
        # 用途：在模板渲染之前修改上下文
        print("7. 模板响应返回之前")
        return response