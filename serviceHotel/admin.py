from django.contrib import admin
from .models import * 


class HotelAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Hotel._meta.fields]

class RoomAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Room._meta.fields]


admin.site.register(Hotel, HotelAdmin)
admin.site.register(Room, RoomAdmin)