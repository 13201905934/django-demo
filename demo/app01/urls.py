from django.contrib import admin
from django.urls import path,re_path
#views为视图文件
#from app01.views import article_create,article_detail,phone_detail
from . import views
urlpatterns = [   
    #浏览器url中通过name值可以直接匹配到 article/create/
    #此为字符串精确匹配模式
    path('create/',views.article_create,name='article_create'),
    #路径转换器模式 <类型：变量>代表通配符 传任何数字都将被 变量接收
    path('<int:article_id>/<str:title>/',views.article_detail,name='article_detail'),
    #正则表达式匹配 注意是：re_path
    re_path('^phone/(?P<phone_number>1[3456789]\d{9})/$',views.phone_detail,name='phone_detail'),
    path('list/',views.list,name='artile_list')
]