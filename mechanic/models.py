from django.db import models

# Create your models here.

"""model to store all the active unaccepted requests"""
class need_help(models.Model):
    name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    contact_no = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    """to send objects to mechanics dashboard through websockets"""
    def get_all_objects(self):
        queryset = self._meta.model.objects.all().values('name', 'user_name', 'email', 'description', 'contact_no', 'latitude', 'longitude')
        # can use the below method also
        # queryset = self.__class__.objects.all()
        return list(queryset)

"""Model to keep track of the orders completed"""
class helps_finished(models.Model):
    customer_name = models.CharField(max_length=100)
    mechanic_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    customer_email = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    customer_contact_no = models.CharField(max_length=100)
    customer_description = models.CharField(max_length=1000)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    customer_latitude = models.CharField(max_length=100)
    customer_longitude = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    is_feedback_given = models.BooleanField(default=False)

    def __str__(self):
        return str(self.mechanic_name) + ' | ' + str(self.customer_name)

    """to send objects to customer page for redirecting him to feedback page for respective mechanic"""
    def get_all_objects(self):
        queryset = self._meta.model.objects.all().values('is_feedback_given', 'created', 'mechanic_name', 'customer_name', 'email', 'customer_email', 'contact_no', 'customer_contact_no', 'latitude', 'customer_latitude', 'longitude', 'customer_longitude')
        # can use the below method also
        # queryset = self.__class__.objects.all()
        return list(queryset)
