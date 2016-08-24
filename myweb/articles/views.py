from django.shortcuts import render

# Create your views here.
def articles_list(request,block_id):
    block_id = int(block_id)
    pass


def articles_list_all(request):
    return render(request,"articles_list_all.html")
