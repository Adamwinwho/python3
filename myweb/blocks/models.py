from django.db import models

# Create your models here.
class Blocks(models.Model):
    name = models.CharField("板块名称",max_length=100)
    manager = models.CharField("管理员",max_length=100)

    create_timestamp = models.DateTimeField("创建时间",auto_now_add=True)
    last_update_timestamp = models.DateTimeField("最近一次更新时间",auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "板块"
        verbose_name_plural = "板块"
