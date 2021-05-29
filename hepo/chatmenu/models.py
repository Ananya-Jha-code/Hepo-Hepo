from django.db import models
from django.contrib import admin


class Room(models.Model):
    name = models.CharField(max_length=1000)


class RoomAdmin(admin.ModelAdmin):
    list_display = ('name',)




class Messages(models.Model):
    username = models.CharField(max_length=100000)

    def __str__(self):
        return self.username







