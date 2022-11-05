from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def index(request):
    posts = Post.objects.all().order_by("-id")[:3]
    # mathiko code latest post aauxa tin ota
    return render(request,'blog/index.html',{'posts':posts})
    # return render(request,'blog/index.html')

    # return HttpResponse("<h1>Hello, world. You're at the polls index.</h1>")

def bindex(request):
    bposts = Post.objects.all()
    return render(request,'blog/blog-list.html',{'bcposts':bposts})

def post_detail(request,id):
    posts = Post.objects.get(id = id)
    return render(request,'blog/post-detail.html',{'post':posts})