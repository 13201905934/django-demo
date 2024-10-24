from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def helloworld(request):
    return HttpResponse('hello world')

#定义文章列表函数
def article_create(request):
    return HttpResponse('创建一篇文章')

#查看文章id
def article_detail(request,article_id,title):
    return HttpResponse(f'文章id是{article_id},标题是{title}')

#展示手机号（浏览器中的）、
def phone_detail(request,phone_number):
    return HttpResponse(f'手机号是{phone_number}')

def list(request):
    author='qiangwengang'
    article_number=20
    #文章列表
    article_list=[
        '第一篇文章,神那么是django',
        '第一篇文章,我想你魏桂容',
        '第一篇文章,不知道你有没有想我'
    ]
    #信息
    info={
        'name':'qiangwengang',
        'age':'26',
        'program_language':['python','java','c']
    }
    return render(request,'list.html',{
        #将上面定义的值返回给html模板
        'author':author,
        'number':article_number,
        'article_list':article_list,
        'info':info
    })