from django.db import models

# Create your models here.

class Location(models.Model):
    user_name = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.latitude},{self.longitude}"

class helps_received(models.Model):
    customer_name = models.CharField(max_length=200)
    mechanic_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    customer_email = models.CharField(max_length=200)
    contact_no = models.CharField(max_length=50)
    customer_contact_no = models.CharField(max_length=50)
    customer_description = models.CharField(max_length=1000)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    customer_latitude = models.CharField(max_length=200)
    customer_longitude = models.CharField(max_length=200)
    avg_rating = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.customer_name)

    def get_all_objects(self):
        queryset = self._meta.model.objects.all().values('avg_rating', 'mechanic_name', 'customer_name', 'email', 'customer_email', 'contact_no', 'customer_contact_no', 'latitude', 'customer_latitude', 'longitude', 'customer_longitude')
        # can use the below method also
        # queryset = self.__class__.objects.all()
        return list(queryset)
