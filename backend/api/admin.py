from django.contrib import admin

from .models import Ping

class PingAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')


admin.site.register(Ping, PingAdmin)
