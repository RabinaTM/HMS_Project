from django.contrib import admin
from .models import Departments, Doctors,Booking,Doctor,Patient,Appointment
# Register your models here.

admin.site.register(Departments)
admin.site.register(Doctors)
admin.site.register(Booking)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)