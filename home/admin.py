from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserProfile, Feedback, Contact
# Register your models here.

admin.site.register(Feedback)
admin.site.register(Contact)

class UserModelAdmin(admin.ModelAdmin):
    readonly_fields = ('date_joined', 'last_login', )
admin.site.unregister(User)
admin.site.register(User, UserModelAdmin)
admin.site.register(UserProfile)
