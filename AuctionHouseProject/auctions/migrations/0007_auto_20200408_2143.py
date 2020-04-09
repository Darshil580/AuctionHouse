# Generated by Django 3.0.4 on 2020-04-08 16:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_auto_20200408_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biddingofproperty',
            name='bid_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 8, 16, 13, 14, 319378, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='currentauction',
            name='auction_end_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='currentauction',
            name='auction_start_date',
            field=models.DateTimeField(null=True),
        ),
    ]