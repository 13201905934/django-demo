from django.db import models
from utils.basemodels import BaseModel

# Create your models here.
#创建模型
class User(BaseModel):
    #创建一个User表 并创建主键id
    id=models.AutoField(primary_key=True)
    username=models.CharField('用户名',max_length=30,null=True,blank=True,unique=True)
    password=models.CharField('密码',max_length=30)
    email=models.EmailField('邮箱',null=True,blank=True,unique=True)

    class Meta:
        db_table='user'
        verbose_name='用户信息'
        #去掉用户信息后面的s
        verbose_name_plural='用户信息'
    
    #返回用户名
    def __str__(self):
        return self.username