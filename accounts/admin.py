from django.contrib import admin
from .models import profile , UserAddress , UserPhoneNumber
# Register your models here.
admin.site.register(profile)
admin.site.register(UserAddress)
admin.site.register(UserPhoneNumber)