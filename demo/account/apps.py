from django.apps import AppConfig


class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'account'
    #将后台页面上的account改为 用户管理
    verbose_name='用户管理'
