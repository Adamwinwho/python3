#!coding=utf-8

#from django.http import HttpResponse
import uuid
import datetime
from django.utils import timezone
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth.models import User
from usercenter.models import ActivateCode

def index(request):
    return render(request,"index.html")

def register(request):
    error = ""
    if request.method == 'GET':
        return render(request,'register.html')
    else:
        name = request.POST['username'].strip()
        passwd = request.POST['passwd'].strip()
        re_passwd = request.POST['re_passwd'].strip()
        email = request.POST['email'].strip()

        if  not name or not email or not passwd or not re_passwd:
            error = "任何字段均不能为空"
        if passwd != re_passwd:
            error = "两次密码不一致"
        if User.objects.filter(username=name).count()>0:
            error = "用户已存在"
        if User.objects.filter(email=email).count()>0:
            error = "改邮箱已被注册"
        if not error:
            user = User.objects.create_user(name,email,passwd)
            user.is_active = False
            user.save()

            new_code = str(uuid.uuid4()).replace("-","")
            #设置激活链接失效时间2天
            expire_time = timezone.now()+datetime.timedelta(days=2)
            #创建实例，激活时查找该用户并设置激活状态
            code_record = ActivateCode(owner=user,code=new_code,expire_timestamp=expire_time)
            code_record.save()
            
            activate_link = "http://%s/activate/%s" % (request.get_host(),new_code)
            activate_email = '''点击<a href="%s">这里</a>激活''' % activate_link

            send_mail(subject='[追风筝的Who]激活邮件',
                      message='点击链接激活: %s' % activate_link,
                      html_message=activate_email,
                      from_email='1137048513@qq.com',
                      recipient_list=[email],
                      fail_silently=False)
        else:
            return render(request,'register.html',{"error":error})
        return render(request,'activate_success.html',{"msg":"注册成功，激活邮件已经发送到你的邮箱，请点击邮箱中的链接完成激活"})
    
    
