from django.urls import path
from .views import create_contact, ContactList

urlpatterns = [
    path("create-contact/", create_contact, name='create-contact'),
    path("contacts/", ContactList.as_view(), name='contact-list'),
]
