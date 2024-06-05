# blog/views.py

from django.shortcuts import render
from .models import Post, Comment, Category

def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    categories = Category.objects.all()

    category_name = request.GET.get('category')
    if category_name:
        posts = posts.filter(categories__name__contains=category_name)

    context = {
        "posts": posts,
        "categories": categories,
    }
    return render(request, "index.html", context)

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by("-created_on")
    categories = Category.objects.all()
    context = {
        "category": category,
        "posts": posts,
        "categories": categories,
    }
    return render(request, "index.html", context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    categories = Category.objects.all()
    context = {
        "post": post,
        "comments": comments,
        "categories": categories,
    }

    return render(request, "detail.html", context)