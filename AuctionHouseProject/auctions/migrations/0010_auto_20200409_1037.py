# Generated by Django 3.0.4 on 2020-04-09 05:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_auto_20200408_2228'),
    ]

    operations = [
        migrations.RenameField(
            model_name='currentauction',
            old_name='property_id',
            new_name='property_reg',
        ),
        migrations.AlterField(
            model_name='biddingofproperty',
            name='bid_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 9, 5, 7, 45, 297475, tzinfo=utc)),
        ),
    ]