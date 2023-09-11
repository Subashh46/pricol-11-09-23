from django.contrib import admin
from .models import Status, Machine, Scan

admin.site.register(Status)
admin.site.register(Machine)
admin.site.register(Scan)
