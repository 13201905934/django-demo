from django.db import models

#数据库中公共的字段 其他表可以来继承
class BaseModel(models.Model):
    # auto_now_add自动更新 editable 可编辑
    create_at=models.DateTimeField('创建时间',auto_now_add=True,editable=True)
    # auto_now 当前时间
    updated_at=models.DateTimeField('更新时间',auto_now=True,editable=True)

    class Meta:
        #声明该表是抽象类 数据迁移时不会生成（本身就是让别的表调用 不需要生成）
        abstract=True