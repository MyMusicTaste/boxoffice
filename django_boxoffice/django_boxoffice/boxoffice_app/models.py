from django.db import models


# Create your models here.
class UpdateLog(models.Model):
    last_update = models.CharField(max_length=128)

    class Admin:
        pass

    def __unicode__(self):
        return self.last_update


class ArtistEvent(models.Model):
    name = models.CharField(max_length=512)

    class Admin:
        pass

    # def __unicode__(self):
    #     return self.name


class City(models.Model):
    name = models.CharField(max_length=256)
    state = models.CharField(max_length=256)

    class Admin:
        pass

    def __unicode__(self):
        return "%s, %s" % (self.name, self.state)


class Venue(models.Model):
    name = models.CharField(max_length=256)

    class Admin:
        pass

    def __unicode__(self):
        return self.name


class Price(models.Model):
    price = models.FloatField()

    class Admin:
        pass

    def __unicode__(self):
        return '$%s' % self.price


class Promoter(models.Model):
    name = models.CharField(max_length=256)

    class Admin:
        pass

    def __unicode__(self):
        return self.name


class Event(models.Model):
    artist_event = models.ForeignKey(ArtistEvent)
    city = models.ForeignKey(City)
    venue = models.ForeignKey(Venue)
    sale = models.FloatField()
    attend = models.IntegerField()
    capacity = models.IntegerField()
    show = models.IntegerField()
    sellout = models.IntegerField()
    rank = models.IntegerField()
    dates = models.CharField(max_length=512)
    create_date = models.CharField(max_length=128)

    class Admin:
        pass

    def __repr__(self):
        return self


class EventPromoter(models.Model):
    class Meta:
        unique_together = (('event', 'promoter'),)

    event = models.ForeignKey(Event)
    promoter = models.ForeignKey(Promoter)

    class Admin:
        pass

    def __unicode__(self):
        return "%s, %s" % (self.event_id, self.promoter_id)


class EventPrice(models.Model):
    class Meta:
        unique_together = (('event', 'price'),)

    event = models.ForeignKey(Event)
    price = models.ForeignKey(Price)

    class Admin:
        pass

    def __unicode__(self):
        return "%s, %s" % (self.event_id, self.price_id)


class Date(models.Model):
    class Meta:
        unique_together = (('event', 'event_date'),)
        # unique_together = (('event', 'year', 'month', 'date'),)

    event = models.ForeignKey(Event)
    event_date = models.DateField()
    # year = models.IntegerField()
    # month = models.IntegerField()
    # date = models.IntegerField()

    class Admin:
        pass

    def __unicode__(self):
        return '"event_id" : "%s", "event_date" : "%s"' % (self.event_id, self.event_date)

    def __repr__(self):
        # return self
        return '"event_id" : "%s", "event_date" : "%s"' % (self.event_id, self.event_date)


class ErrorLog(models.Model):
    table_name = models.CharField(max_length=256)
    artist_event = models.CharField(max_length=512)
    city = models.CharField(max_length=256)
    venue = models.CharField(max_length=256)
    attend_capacity = models.CharField(max_length=256)
    gross_sales = models.CharField(max_length=256)
    show_sellout = models.CharField(max_length=256)
    rank = models.CharField(max_length=256)
    dates = models.CharField(max_length=512)
    prices = models.CharField(max_length=256)
    promoters = models.CharField(max_length=512)
    create_date = models.CharField(max_length=128)

    class Admin:
        pass

    def __unicode__(self):
        return self.table_name

