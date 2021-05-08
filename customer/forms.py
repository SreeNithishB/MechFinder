from django import forms
from .models import Location

class LocationModelForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('latitude', 'longitude')
        widgets = {
            'latitude': forms.TextInput(attrs={'id': 'latitude_id'}),
            'longitude': forms.TextInput(attrs={'id': 'longitude_id'}),
        }
        labels = {
            'latitude': "",
            'longitude': "",
        }

class AskHelpForm(forms.Form):
    name = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'name_AskHelpForm'}))
    user_name = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'userName_AskHelpForm'}))
    email = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'email_AskHelpForm'}))
    description = forms.CharField(label='', max_length=1000, widget= forms.Textarea(attrs={'id':'description_AskHelpForm',
                                                                                        'style': 'height: 200px;width:500px',
                                                                                        'placeholder': "Please type your concerns here.",}))
    contact_no = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'contact_no_AskHelpForm'}))

class GetDetailsForFeedback(forms.Form):
    customer_name = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'customer_name_GetDetailsForFeedback'}))
    mechanic_name = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'mechanic_name_GetDetailsForFeedback'}))
    email = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'email_GetDetailsForFeedback'}))
    customer_email = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'customer_email_GetDetailsForFeedback'}))
    contact_no = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'contact_no_GetDetailsForFeedback'}))
    customer_contact_no = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'customer_contact_no_GetDetailsForFeedback'}))
