from django.urls import path
#views为视图文件
from . import views
urlpatterns = [   
    path('login/',views.login),
    #类视图匹配
    path('register/',views.RegisterView.as_view()),
]