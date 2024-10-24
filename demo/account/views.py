from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View

# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        #业务逻辑判断等操作
        #定义一个响应对象
        headers={
           'token':'qiangwengang'
        }
        #return HttpResponse(f'用户名{username}的密码是{password}',headers=headers,status=200)
        #返回JsonResponse
        res={
           'name':username,
           'password':password,
           'status':200,
           'message':'OK'
        }
        return JsonResponse(res)
    elif request.method=='GET':
     #禁止访问的ip列表
     #FORBIDDEN_IP=['127.0.0.1','0.0.0.000']
     #用户访问的IP地址
     #if request.META.get('REMOTE_ADDR') in FORBIDDEN_IP:
        #return HttpResponse('请求异常')
    #返回登录页
     return render(request,'login.html')
 
#类视图 实现一个注册功能
class RegisterView(View):
   #设置get请求方法
   def get(self,request):
      return render(request,'register.html')
   #设置post请求方法
   def post(self,request):
      username=request.POST.get('username')
      password=request.POST.get('password')
      password2=request.POST.get('password2')
      return HttpResponse(f'用户名{username}的密码是{password}')
