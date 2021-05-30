from django.contrib import admin
from .models import Room, RoomAdmin, Messages


admin.site.register(Room, RoomAdmin)
admin.site.register(Messages)