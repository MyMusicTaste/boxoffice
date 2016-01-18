# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=100)),
                ('slug', models.TextField(max_length=100)),
                ('category', models.TextField(max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ClientRepresentatives',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('representative_type', models.TextField(max_length=30)),
                ('name', models.TextField(max_length=100)),
                ('booking_price', models.TextField(max_length=30)),
                ('client', models.ForeignKey(to='booking_app.Client')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Representatives',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=100)),
                ('slug', models.TextField(max_length=100)),
                ('company', models.TextField(max_length=100)),
                ('phone_number', models.TextField(max_length=30)),
                ('email_address', models.TextField(max_length=100)),
                ('mailing_address', models.TextField(max_length=200)),
                ('role', models.TextField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='clientrepresentatives',
            name='representative',
            field=models.ForeignKey(to='booking_app.Representatives'),
            preserve_default=True,
        ),
    ]
