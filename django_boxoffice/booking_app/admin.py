from django.contrib import admin
from .models import Client
from .models import Representatives
from .models import ClientRepresentatives


@admin.register(Client)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'category',)
    list_select_related = True


# admin.site.register(Client)
admin.site.register(Representatives)
admin.site.register(ClientRepresentatives)
