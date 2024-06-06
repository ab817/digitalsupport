# blog/views.py

from django.shortcuts import render
#from django.views.decorators.csrf import csrf_exempt

from .models import Post, Comment, Category

#@csrf_exempt
def search(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    if request.method == "POST":
        searched = request.POST['searched']
        posts = Post.objects.filter(title__icontains = searched)
        return render(request, 'search.html', {'posts': posts, 'categories': categories, 'searched':searched})
    else:
        return render(request, 'search.html', {'posts': posts, 'categories': categories})
    """
    q = request.GET.get('q')
    if q:
        posts = posts.filter(title__icontains=q) | posts.filter(body__icontains=q)

    category = request.GET.get('category')
    if category:
        posts = posts.filter(categories__name=category)
    """


def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    categories = Category.objects.all()
    current_posts = Post.objects.filter(categories__name='Current')[:2]

    category_name = request.GET.get('category')
    if category_name:
        posts = posts.filter(categories__name__contains=category_name)

    context = {
        "posts": posts,
        "categories": categories,
        'current_posts': current_posts,
    }
    return render(request, "index.html", context)

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by("-created_on")
    categories = Category.objects.all()
    current_posts = Post.objects.filter(categories__name='Current')[:2]
    context = {
        "category": category,
        "posts": posts,
        "categories": categories,
        'current_posts': current_posts,
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

"""
def blog_view(request):
    current_posts = Post.objects.filter(categories__name='Current')[:2]
    all_posts = Post.objects.all()
    categories = Category.objects.all()
    return render(request, 'index.html', {
        'current_posts': current_posts,
        'posts': all_posts,
        'categories': categories,
    })
"""