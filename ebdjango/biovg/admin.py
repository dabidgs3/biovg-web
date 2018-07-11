from django.contrib import admin

# Register your models here.
from .models import Header, Service_Section

admin.site.register(Header)
admin.site.register(Service_Section)