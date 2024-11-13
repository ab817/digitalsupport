from django.shortcuts import render
from .models import Contact, TelephoneLine, ContactInfo , ManagerContact
from django.core.paginator import Paginator
from django.db.models import Q
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

def managercontact_list(request):
    query = request.GET.get('q', '')  # Default to an empty string if 'q' is not provided
    if query:
        #contacts = ManagerContact.objects.filter(branch__icontains=query) | ManagerContact.objects.filter(region__icontains=query | ManagerContact.objects.filter(mobile_number__icontains=query))
        contacts = ManagerContact.objects.filter(
                        Q(branch__icontains=query) |
                        Q(region__icontains=query) |
                        Q(mobile_number__icontains=query)
                    )
    else:
        contacts = ManagerContact.objects.all()

    # Order the queryset
    contacts = contacts.order_by('branch')

    paginator = Paginator(contacts, 20)  # 20 contacts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Debugging
    #print(f"Total contacts: {contacts.count()}")
    #print(f"Query: {query}")
    #print(f"Page number: {page_number}")
    #print(f"Page object: {page_obj}")

    return render(request, 'managercontact_list.html', {'page_obj': page_obj, 'query': query})

def telephone_lines(request):
    telephone_lines = TelephoneLine.objects.all()
    return render(request, 'telephone_lines.html', {'telephone_lines': telephone_lines})


def contact_card_view(request):
    contacts = ContactInfo.objects.all()
    return render(request, 'contactcard.html', {'contacts': contacts})
