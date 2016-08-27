from django.shortcuts import render
from blocks.models import Blocks
from .models import Articles

# Create your views here.
def articles_list(request,block_id):
    block_id = int(block_id)
    block = Blocks.objects.get(id=block_id)
    blocks_info = Blocks.objects.all().order_by("id")
    articles_list = Articles.objects.filter(block=block).order_by("-id")
    return render(request,"articles_list.html",{"articles":articles_list,"blocks":blocks_info})


def articles_list_all(request):
    blocks_info = Blocks.objects.all().order_by("id")
    articles_info = Articles.objects.all().order_by("-id")
    return render(request,"articles_list_all.html",{"blocks":blocks_info,"articles":
        articles_info})


def article_detail(request,article_id):
    article_id = int(article_id)
    blocks_info = Blocks.objects.all().order_by("id")
    article = Articles.objects.get(id=article_id)
    return render(request,"article_detail.html",{"blocks":blocks_info,"article":article})
