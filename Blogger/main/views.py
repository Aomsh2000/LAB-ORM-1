from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from posts.models import Post
# Create your views here.

def home_page_view(request:HttpRequest):

    #get all posts
    posts = Post.objects.all().order_by("-published_at")[0:4]

    return render(request,'main/home.html',{"posts":posts})

