# blog/views.py
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
#from django.views.decorators.csrf import csrf_exempt

from .models import Post, Comment, Category, PortalSetting


#@csrf_exempt
def search(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    searched = None
    paginated_posts = None

    if request.method == "POST":
        searched = request.POST['searched']
        posts = Post.objects.filter(title__icontains=searched)

        paginator = Paginator(posts, 5)  # Show 5 posts per page
        page = request.GET.get('page')

        try:
            paginated_posts = paginator.page(page)
        except PageNotAnInteger:
            paginated_posts = paginator.page(1)
        except EmptyPage:
            paginated_posts = paginator.page(paginator.num_pages)

    return render(request, 'search.html', {
        'posts': paginated_posts,
        'categories': categories,
        'searched': searched
    })


def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    categories = Category.objects.all()
    current_posts = Post.objects.filter(categories__name='Current')[:2]

    paginator = Paginator(posts, 5)  # Show 5 posts per page
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

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

    paginator = Paginator(posts, 5)  # Show 5 posts per page
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

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

def portal(request):
    setting = PortalSetting.objects.first()
    show_popup = setting.show_popup if setting else False
    popup_image = setting.popup_image.url if setting and setting.popup_image else ''
    #show_image = setting.show_image if setting else False
    return render(request, 'portal.html', {
        'show_popup': show_popup,
        'popup_image': popup_image,
       # 'show_image': show_image
    })