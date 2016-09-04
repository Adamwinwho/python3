#coding:utf-8

from django.shortcuts import render
from usercenter.models import ActivateCode
from django.utils import timezone
# Create your views here.

def activate(request,code):
    #找到注册时创建的实例，设置激活状态
    acts = ActivateCode.objects.filter(code=code,expire_timestamp__gte=timezone.now())
    if acts.count()>0:
        code_record = acts[0]
        code_record.owner.is_active = True
        code_record.save()
        return render(request,"activate_status.html",{"msg":"激活成功","msg2":"登陆试试吧","link":"#"})
    else:
        return render(request,"activate_status.html",{"msg":"激活失败"})

