from .models import UserProfile, Contact, Feedback
from django.forms import ModelForm
from django import forms
#from phonenumber_field.formfields import PhoneNumberField

#class ClientForm(forms.Form):
#    phone = PhoneNumberField()

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['firstname', 'lastname', 'email', 'phone', 'isMech']
        labels = {
            'firstname': "First Name",
            'lastname': "Last name",
            'email' : "Email id",
            'phone' : "Phone Number",
            'isMech' : "Are you a mechanic? "
        }

        widgets = {
            'firstname': forms.TextInput(attrs={'placeholder': 'First name'}),
            'lastname': forms.TextInput(attrs={'placeholder': 'Last name'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Ex: +91 abc-def-ghij'}),
            'email': forms.TextInput(attrs={'placeholder': 'Ex: xyz@example.com'}),
        }


class FeedbackModelForm(ModelForm):

    class Meta:
        model = Feedback
        fields = {'rating', 'message'}
        CHOICES= (
                    ('1','NOT SATISFIED'),
                    ('2','JUST OK'),
                    ('3','GOOD'),
                    ('4','SUPER'),
                    ('5','EXCELLENT'),
                 )
        widgets = {
            'rating': forms.Select(choices=CHOICES,attrs={'class':'form-select'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Optional.'}),
        }
        labels = {
            'rating': "Rating",
            'message': "Message",
        }
        


class ContactModelForm(ModelForm):
    class Meta:
        model = Contact
        fields = {'name','email','message'}
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'})
        }

        labels = {
            'name': "Name",
            'email': "Email",
            'message': "Your opinion"
        }
