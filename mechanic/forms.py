from django import forms

"""Forms to calculate route using google maps"""
class DirectionForm(forms.Form):
    m_lat = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'m_lat'}))
    m_lon = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'m_lon'}))
    c_lat = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'c_lat'}))
    c_lon = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'c_lon'}))

"""Forms to collect data to be stored in helps_received database"""
class HelpsReceivedForm(forms.Form):
    customer_name = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'customer_name_HelpsReceivedForm'}))
    mechanic_name = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'mechanic_name_HelpsReceivedForm'}))
    email = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'email_HelpsReceivedForm'}))
    customer_email = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'customer_email_HelpsReceivedForm'}))
    contact_no = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'contact_no_HelpsReceivedForm'}))
    customer_contact_no = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'customer_contact_no_HelpsReceivedForm'}))
    customer_description = forms.CharField(label='', max_length=1000, widget= forms.TextInput(attrs={'id':'customer_description_HelpsReceivedForm'}))
    latitude = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'latitude_HelpsReceivedForm'}))
    longitude = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'longitude_HelpsReceivedForm'}))
    customer_latitude = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'customer_latitude_HelpsReceivedForm'}))
    customer_longitude = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'customer_longitude_HelpsReceivedForm'}))

"""Forms to collect the details about the order to be cancelled and rebroadcasted"""
class CancelOrderForm(forms.Form):
    customer_name = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'customer_name_CancelOrderForm'}))
    mechanic_name = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'mechanic_name_CancelOrderForm'}))
    email = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'email_CancelOrderForm'}))
    customer_email = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'customer_email_CancelOrderForm'}))
    contact_no = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'contact_no_CancelOrderForm'}))
    customer_contact_no = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'customer_contact_no_CancelOrderForm'}))
    customer_description = forms.CharField(label='', max_length=1000, widget= forms.TextInput(attrs={'id':'customer_description_CancelOrderForm'}))
    latitude = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'latitude_CancelOrderForm'}))
    longitude = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'longitude_CancelOrderForm'}))
    customer_latitude = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'customer_latitude_CancelOrderForm'}))
    customer_longitude = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'customer_longitude_CancelOrderForm'}))

"""Forms to collect the details of orders to be finished"""
class FinishOrderForm(forms.Form):
    customer_name = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'customer_name_FinishOrderForm'}))
    mechanic_name = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'mechanic_name_FinishOrderForm'}))
    email = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'email_FinishOrderForm'}))
    customer_email = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'customer_email_FinishOrderForm'}))
    contact_no = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'contact_no_FinishOrderForm'}))
    customer_contact_no = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'customer_contact_no_FinishOrderForm'}))
    customer_description = forms.CharField(label='', max_length=1000, widget= forms.TextInput(attrs={'id':'customer_description_FinishOrderForm'}))
    latitude = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'latitude_FinishOrderForm'}))
    longitude = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'longitude_FinishOrderForm'}))
    customer_latitude = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'customer_latitude_FinishOrderForm'}))
    customer_longitude = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'customer_longitude_FinishOrderForm'}))
