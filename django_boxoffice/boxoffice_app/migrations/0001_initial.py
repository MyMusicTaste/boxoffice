# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArtistEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=512)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('state', models.CharField(max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event_date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ErrorLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('table_name', models.CharField(max_length=256)),
                ('artist_event', models.CharField(max_length=512)),
                ('city', models.CharField(max_length=256)),
                ('venue', models.CharField(max_length=256)),
                ('attend_capacity', models.CharField(max_length=256)),
                ('gross_sales', models.CharField(max_length=256)),
                ('show_sellout', models.CharField(max_length=256)),
                ('rank', models.CharField(max_length=256)),
                ('dates', models.CharField(max_length=512)),
                ('prices', models.CharField(max_length=256)),
                ('promoters', models.CharField(max_length=512)),
                ('create_date', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sale', models.FloatField()),
                ('attend', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('show', models.IntegerField()),
                ('sellout', models.IntegerField()),
                ('rank', models.IntegerField()),
                ('dates', models.CharField(max_length=512)),
                ('create_date', models.CharField(max_length=128)),
                ('artist_event', models.ForeignKey(to='boxoffice_app.ArtistEvent')),
                ('city', models.ForeignKey(to='boxoffice_app.City')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventPrice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event', models.ForeignKey(related_name='price', to='boxoffice_app.Event')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventPromoter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event', models.ForeignKey(related_name='promoters', to='boxoffice_app.Event')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Promoter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UpdateLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_update', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='eventpromoter',
            name='promoter',
            field=models.ForeignKey(to='boxoffice_app.Promoter'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='eventpromoter',
            unique_together=set([('event', 'promoter')]),
        ),
        migrations.AddField(
            model_name='eventprice',
            name='price',
            field=models.ForeignKey(to='boxoffice_app.Price'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='eventprice',
            unique_together=set([('event', 'price')]),
        ),
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.ForeignKey(to='boxoffice_app.Venue'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='date',
            name='event',
            field=models.ForeignKey(to='boxoffice_app.Event'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='date',
            unique_together=set([('event', 'event_date')]),
        ),
    ]
