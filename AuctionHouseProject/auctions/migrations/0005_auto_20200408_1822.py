# Generated by Django 3.0.4 on 2020-04-08 12:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20200408_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biddingofproperty',
            name='bid_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 8, 12, 52, 12, 357949, tzinfo=utc)),
        ),
    ]