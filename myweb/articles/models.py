from django.db import models
from blocks.models import Blocks

# Create your models here.

class Articles(models.Model):
    block = models.ForeignKey(Blocks,verbose_name="板块",default=0)
    title = models.CharField("文章标题",max_length=100)
    author = models.CharField("文章作者",max_length=100)
    content = models.CharField("文章内容",max_length=10000)

    last_update_timestamp = models.DateTimeField("最后更新时间",auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = "文章"
