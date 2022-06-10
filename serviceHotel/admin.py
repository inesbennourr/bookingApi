from django.contrib import admin
from .models import * 
# Register your models here.
class HotelAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Hotel._meta.fields]

admin.site.register(Hotel, HotelAdmin)