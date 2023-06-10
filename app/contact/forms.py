from .models import Contact

from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        fields = ['name', 'phone']
        model = Contact
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'phone': forms.TextInput(attrs={"class": "form-control"}),
        }
