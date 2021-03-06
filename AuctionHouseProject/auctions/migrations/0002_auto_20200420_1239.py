# Generated by Django 3.0.4 on 2020-04-20 07:09

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuctionManager',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('user_type', models.CharField(default='AuctionManager', max_length=20)),
            ],
            options={
                'verbose_name': 'AuctionManager',
                'verbose_name_plural': 'AuctionManagers',
            },
            bases=('auth.user', models.Model),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=13)),
                ('message', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='biddingofproperty',
            name='user_bid_amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='currentauction',
            name='current_ending_time',
            field=models.DateTimeField(null=True),
        ),
    ]
