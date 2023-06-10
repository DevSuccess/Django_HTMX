from django.urls import path
from .views import create_contact, ContactList

app_name = 'contact'
urlpatterns = [
    path("create-contact/", create_contact, name='create-contact'),
    path("contacts/", ContactList.as_view(), name='contact-list'),
]
