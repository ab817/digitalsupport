from django.shortcuts import render
from .models import Contact
from django.core.paginator import Paginator
from django.db.models import Q


def contact_list(request):
    query = request.GET.get('q')
    if query:
        contacts = Contact.objects.filter(Q(name__icontains=query) | Q(code__icontains=query))
    else:
        contacts = Contact.objects.all()

    paginator = Paginator(contacts, 3)  # Show 20 contacts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'contact_list.html', {'page_obj': page_obj, 'query': query})
