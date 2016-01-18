from django.db import models

# Create your models here.


class Client(models.Model):
    name = models.TextField(max_length=100)
    slug = models.TextField(max_length=100)
    category = models.TextField(max_length=300)

    class Admin:
        pass

    def nullCount(self):
        count = 0
        if self.name:
            count += 1

        if self.slug:
            count += 1

        if self.category:
            count += 1

        return count

class Representatives(models.Model):
    name = models.TextField(max_length=100)
    slug = models.TextField(max_length=100)
    company = models.TextField(max_length=100)
    phone_number = models.TextField(max_length=30)
    email_address = models.TextField(max_length=100)
    mailing_address = models.TextField(max_length=200)
    role = models.TextField(max_length=200)

    class Admin:
        pass

    def nullCount(self):
        count = 0
        if self.name:
            count += 1

        if self.slug:
            count += 1

        if self.company:
            count += 1

        if self.phone_number:
            count += 1

        if self.email_address:
            count += 1

        if self.mailing_address:
            count += 1

        if self.role:
            count += 1

        return count


class ClientRepresentatives(models.Model):
    client = models.ForeignKey(Client)
    representative = models.ForeignKey(Representatives)
    representative_type = models.TextField(max_length=30)
    name = models.TextField(max_length=100)
    booking_price = models.TextField(max_length=30)

    class Admin:
        pass