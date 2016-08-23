from django.db import models

# Create your models here.

class Articles(models.Model):
    title = models.CharField("文章标题",max_length=100)
    author = models.CharField("文章作者",max_length=100)
    content = models.CharField("文章内容",max_length=10000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = "文章"
