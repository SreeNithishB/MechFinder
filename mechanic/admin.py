from django.contrib import admin
from .models import need_help, helps_finished
# Register your models here.

admin.site.register(need_help)
admin.site.register(helps_finished)
