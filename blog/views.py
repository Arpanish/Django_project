from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def index(request):
    posts = Post.objects.all()
    return render(request,'blog/index.html',{'posts':posts})
    # return render(request,'blog/index.html')

    # return HttpResponse("<h1>Hello, world. You're at the polls index.</h1>")