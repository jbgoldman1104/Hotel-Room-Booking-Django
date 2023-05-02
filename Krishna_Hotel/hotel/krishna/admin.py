from django.contrib import admin
from .models import Hotels,Rooms,Reservation
# Register your models here.
admin.site.register(Hotels)
admin.site.register(Rooms)
admin.site.register(Reservation)