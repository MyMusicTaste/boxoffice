from django.contrib import admin

from .models import ArtistEvent
from .models import City
from .models import Venue
from .models import Promoter
from .models import Price
from .models import Event
from .models import EventPrice
from .models import EventPromoter
from .models import Date
from .models import ErrorLog
from .models import UpdateLog


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('artist_event', 'city', 'dates',)
    search_fields = ('artist_event__name', )
    list_filter = ('city', )
    # raw_id_fields = ('artist', 'city', )
    readonly_fields = ['artist_event', 'city', 'venue', 'sale', 'attend']

    list_select_related = True



# Register your models here.
admin.site.register(UpdateLog)
admin.site.register(ArtistEvent)
admin.site.register(City)
admin.site.register(Venue)
admin.site.register(Promoter)
admin.site.register(Price)
# admin.site.register(Event)
admin.site.register(EventPrice)
admin.site.register(EventPromoter)
admin.site.register(Date)
admin.site.register(ErrorLog)

