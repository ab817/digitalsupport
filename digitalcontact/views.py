from django.shortcuts import render
from .models import Contact
from django.core.paginator import Paginator

def contact_list(request):
    query = request.GET.get('q')
    if query:
        contacts = Contact.objects.filter(name__icontains=query) | Contact.objects.filter(code__icontains=query)
    else:
        contacts = Contact.objects.all().order_by('name')

    paginator = Paginator(contacts, 20)  # 20 contacts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'contact_list.html', {'page_obj': page_obj, 'query': query})