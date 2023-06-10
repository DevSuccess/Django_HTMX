from django.urls import path
from .views import create_contact, delete_contact, ContactList

app_name = 'contact'
urlpatterns = [
    path("", ContactList.as_view(), name='contact-list'),
    path("create/", create_contact, name='create-contact'),
    path("delete/", delete_contact, name='delete-contact'),
]
