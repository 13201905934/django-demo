from django.contrib import admin
from app01.models import Article
# Register your models here.
#定义获取作者的一个函数
def get_author(obj):
    return obj.user.username

class ArticleAdmin(admin.ModelAdmin):
    #配置后台展示列表 将上述获取作者的函数写在里边就可以展示作者
    list_display=('id','title','content','publish_date',get_author)
    #配置过滤字段
    list_filter=('title','publish_date')
    #配置搜索信息
    search_fields=('title','publish_date')
    #只读属性 id不能被修改
    readonly_fields=('id',)
    #配置链接
    list_display_links=('id','title')
    #可以修改
    #list_editable=('title','content')
# 将get_author改为作者
get_author.short_description='作者'

admin.site.register(Article,ArticleAdmin)

