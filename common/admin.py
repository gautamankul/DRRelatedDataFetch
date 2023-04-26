from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(TruckList)
admin.site.register(DispatchAdvice)
admin.site.register(DATruckList)