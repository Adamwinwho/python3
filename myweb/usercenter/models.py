from django.db import models

# Create your models here.
class UserCenter(models.Model):
    name = models.CharField("用户名",max_length=100)
    passwd = models.CharField("密码",max_length=100)
    email = models.CharField("邮箱",max_length=100)
    re_passwd = models.CharField("重复密码",max_length=100)
