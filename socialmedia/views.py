from django.shortcuts import render
from posts.models import Post

def HomePage(request):
    print(f"user is loggined? {request.user.is_authenticated}")
    posts = Post.objects.all()
    return render(request, "index.html", {'posts': posts})

