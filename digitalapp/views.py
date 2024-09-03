# blog/views.py
from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
#from django.views.decorators.csrf import csrf_exempt

from .models import Post, Comment, Category, PortalSetting, Feedback, DigitalProduct


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

def portal(request):
    setting = PortalSetting.objects.first()
    show_popup = setting.show_popup if setting else False
    popup_image = setting.popup_image.url if setting and setting.popup_image else ''
    #show_image = setting.show_image if setting else False
    return render(request, 'portal.html', {
        'show_popup': show_popup,
        'popup_image': popup_image,
        'WHISTLE_BLOWER_URL': settings.WHISTLE_BLOWER_URL,
       # 'show_image': show_image
    })


@csrf_protect
def submit_feedback(request):
    if request.method == 'POST':
        feedback_text = request.POST['feedbackText']
        questioned_by = request.POST['questionedBy']

        # Save the feedback to the database
        feedback = Feedback(feedback_text=feedback_text, questioned_by=questioned_by)
        feedback.save()

        # Add a success message
        messages.success(request, 'Your feedback has been submitted successfully!')

        # Redirect to the same page to display the message in the sidebar
        return redirect(request.META.get('HTTP_REFERER', 'blog_index'))

    return render(request, 'detail.html')

@login_required
def faq_feedback(request):
    feedback_list = Feedback.objects.all().order_by('-submitted_on')  # Order by submission date, latest first
    paginator = Paginator(feedback_list, 10)  # Show 10 feedbacks per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'faq_feedback.html', {'page_obj': page_obj})

def digital_products(request):
    products = DigitalProduct.objects.all()
    return render(request, 'digitalproducts.html', {'products': products})

def digital_product_detail(request, product_id):
    product = get_object_or_404(DigitalProduct, id=product_id)
    return render(request, 'digitalproductdetail.html', {'product': product})

