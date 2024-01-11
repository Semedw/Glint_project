from django import forms

from core.models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            'first_name' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'First Name' }),
            'last_name' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Last Name' }),
            'email' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'E-mail' }),
            'message' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Message' }),
        }