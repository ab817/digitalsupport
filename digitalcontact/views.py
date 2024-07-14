from django.shortcuts import render
from .models import Contact, TelephoneLine
from django.core.paginator import Paginator

def contact_list(request):
    query = request.GET.get('q', '')  # Default to an empty string if 'q' is not provided
    if query:
        contacts = Contact.objects.filter(name__icontains=query) | Contact.objects.filter(code__icontains=query)
    else:
        contacts = Contact.objects.all()

    # Order the queryset
    contacts = contacts.order_by('name')

    paginator = Paginator(contacts, 20)  # 20 contacts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Debugging
    #print(f"Total contacts: {contacts.count()}")
    #print(f"Query: {query}")
    #print(f"Page number: {page_number}")
    #print(f"Page object: {page_obj}")

    return render(request, 'contact_list.html', {'page_obj': page_obj, 'query': query})

def telephone_lines(request):
    telephone_lines = TelephoneLine.objects.all()
    return render(request, 'telephone_lines.html', {'telephone_lines': telephone_lines})
