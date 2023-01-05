from django.shortcuts import render, redirect
from django.views import View
from django.contrib.messages import success, error
from django.shortcuts import HttpResponse
from django.http.response import JsonResponse
from django.db.models import Q
from .forms import PostForm, CommentForm
from .models import Post, Comment
from users.models import ProfileModel, UserModel
# Create your views here.

class AddPostView(View):

    def get(self, request):

        if not request.user.is_authenticated:
            error(request, 'You have to login into your account first!', extra_tags="danger")
            return redirect('index_url')

        post_form = PostForm()
        return render(request, 'posts/addpost.html', {'post_form': post_form})

    def post(self, request):

        post_form = PostForm(request.POST, files=request.FILES)

        if (post_form.is_valid()):

            instance =  post_form.save(commit=False)
            instance.author = request.user
            instance.save()

            success(request, 'your post has added with successfully!', extra_tags="secondary")
    
        return redirect('index_url')
        

def PostDetailView(request, id):
    post = Post.objects.get(pk=id)
    try: 
        comment = Comment.objects.filter(post=post)
        comment_form = CommentForm()
        print(comment)
        print('comment')

        return render(request, 'posts/post.html', {'post':post, 'comment_form': comment_form, 'comments': comment})
    except:
        comment_form = CommentForm()
        print(post.author.followers.all())

        return render(request, 'posts/post.html', {'post':post, 'comment_form': comment_form})

def LikeView(request, id):

    if request.user.is_authenticated:
        post = Post.objects.get(id=id)
        if request.user in post.likes.all():
            post.likes.remove(request.user)
            return JsonResponse({'sit':0})
        else:
            post.likes.add(request.user)
            return JsonResponse({'sit':1})
    else:
        return JsonResponse({'sit':2})

def search_results(request):

    query = request.GET.get("q")
    objs = Post.objects.filter(
        Q(title__icontains = query) | Q(description__icontains = query)
    )

    return render(request, "index.html", {'posts': objs})

class CommentView(View):

    def get(self, request):
        return redirect(request.META.get("HTTP_REFERER"))
    
    def post(self, request, id):
        comment = CommentForm(request.POST)
        if comment.is_valid:
            instance = comment.save(commit=False)
            instance.author = request.user
            instance.post = Post.objects.get(id=id)
            instance.save()
            return redirect(request.META.get("HTTP_REFERER"))