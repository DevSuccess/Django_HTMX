from django.shortcuts import render
from .models import Contact
from django.views.generic.list import ListView


# Create your views here.
def create_contact(request):
    name = request.POST.get('name')
    phone = request.POST.get('phone')

    contact = Contact.objects.create(name=name, phone=phone)
    contacts = Contact.objects.all()

    context = {
        'contacts': contacts
    }
    return render(request, 'contact/contact-list.html', context)


class ContactList(ListView):
    template_name = 'contact/contact.html'
    model = Contact
    context_object_name = 'contacts'
