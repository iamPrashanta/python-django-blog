from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.http import HttpResponse

# def home(request):
    # return HttpResponse("Welcome to the Blog!")
    # return render(request, 'blog/home.html')

def homepage(request):
    posts = Post.objects.all().order_by('-published_at')
    return render(request, 'blog/home.html', {'posts': posts})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blog/form.html', {'form': form, 'title': 'Create Post'})

def update_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/form.html', {'form': form, 'title': 'Edit Post'})

def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('home')