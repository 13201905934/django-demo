from django.contrib import admin
#导入User模型
from account.models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    #展示username email
    list_display=('username','email')
    #配置过滤字段
    list_filter=('username','email')
    #配置搜索信息
    search_fields=('username','email')

#将user模型绑定到UserAdmin
admin.site.register(User,UserAdmin)
