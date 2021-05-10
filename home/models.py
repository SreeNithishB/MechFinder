from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.urls import reverse
#from phonenumber_field.modelfields import PhoneNumberField
#from phone_field import PhoneField


class UserProfile(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, related_name='profile')
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20) #PhoneNumberField(null=False, blank=False, unique=True)
    #phone_number = PhoneField(blank=True, help_text='Contact phone number')
    #phone = PhoneNumberField()
    isMech = models.BooleanField(default=False)

    class Meta:
        ordering = ['-isMech',]

    def __str__(self):
        return self.firstname


CHOICES= [
               ('1','NOT SATISFIED'),
               ('2','JUST OK'),
               ('3','GOOD'),
               ('4','SUPER'),
               ('5','EXCELLENT'),

          ]
# Create your models here.
class Feedback(models.Model):
#    mech_name = models.ForeignKey(User, on_delete=models.CASCADE)
#    cust_name = models.ForeignKey(User, on_delete=models.CASCADE)

    customer_name = models.CharField(max_length=100)
    mechanic_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    customer_email = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    customer_contact_no = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    rating = models.CharField(max_length = 1,choices = CHOICES, default='3')
    message = models.CharField(max_length = 200, blank=True)

    def __str__(self):
        return self.mechanic_name + ' | ' + self.customer_name

#    def get_absolute_url(self):
#        return reverse('Mech:home-submited')

class Contact(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()
    message = models.TextField(default="")
    def __str__(self):
          return self.name
#    def get_absolute_url(self):
#         return reverse('Mech:home-contact')
