from django.db import models
from account.models import User
#导入公共表字段 在下面调用
from utils.basemodels import BaseModel

# Create your models here.
# 创建好后要映射到数据库上 就要使用数据迁移：python manage.py makemigrations(生成迁移文件) python manage.py migrate(迁移数据库)
class Article(BaseModel):
    id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=120)
    content=models.TextField()
    publish_date=models.DateTimeField()
    #设置外键，和user表关联 一个user可以写多篇文章 on_delete=models.CASCADE:作者被删除 那么关联的文章也会被自动删除
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        #表名
        db_table='article'
        verbose_name='文章信息'
        #按发布时间降序排列 
        ordering=['-publish_date']
        verbose_name_plural='文章信息'