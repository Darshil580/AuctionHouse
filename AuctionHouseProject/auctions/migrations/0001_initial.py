# Generated by Django 3.0.4 on 2020-04-02 06:20

import auctions.models
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgentUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('user_type', models.CharField(default='agent', max_length=10)),
                ('address', models.TextField(max_length=255)),
                ('pincode', models.CharField(default='000000', max_length=6)),
                ('mobile', models.CharField(max_length=255)),
                ('birth_date', models.DateField(blank=True)),
                ('proof_document', models.FileField(blank=True, upload_to='agent_proof_document')),
                ('resume_document', models.FileField(blank=True, upload_to='agent_resume_document')),
                ('image', models.ImageField(blank=True, upload_to='agent_image')),
                ('interview_date', models.DateTimeField(blank=True)),
                ('interviewed', models.BooleanField(blank=True, default=False)),
                ('contacted', models.BooleanField(default=True)),
                ('approved', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'AgentUser',
                'verbose_name_plural': 'AgentUsers',
            },
            bases=('auth.user', models.Model),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CurrentAuction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_fees', models.IntegerField()),
                ('auction_start_date', models.DateTimeField()),
                ('auction_end_date', models.DateTimeField()),
                ('increment_ratio', models.FloatField()),
                ('current_amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propery_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('profile_setup', models.BooleanField(default=False)),
                ('user_type', models.CharField(default='user', max_length=10)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user', models.Model),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(default='To be Setup', max_length=255)),
                ('mobile', models.CharField(default='To be Setup', max_length=13)),
                ('birth_date', models.DateField(blank=True)),
                ('pincode', models.CharField(default='000000', max_length=6)),
                ('image', models.ImageField(blank=True, upload_to='profile_pics')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.City')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.State')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auctions.User')),
            ],
        ),
        migrations.CreateModel(
            name='RegForAuction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_status', models.CharField(max_length=12)),
                ('current_auction_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current_auction', to='auctions.CurrentAuction')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='register', to='auctions.User')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyReg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_address', models.CharField(max_length=255)),
                ('pincode', models.CharField(default='000000', max_length=6)),
                ('property_description', models.CharField(default='', max_length=2000)),
                ('approved_date', models.DateTimeField()),
                ('approved', models.BooleanField(default=False)),
                ('pre_set_amount', models.IntegerField(default=0)),
                ('scheduled_status', models.BooleanField(default=False)),
                ('current_auction_status', models.BooleanField(default=False)),
                ('viewinghours', models.CharField(default='None2', max_length=20)),
                ('agent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='who_approves', to='auctions.AgentUser')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.City')),
                ('property_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property', to='auctions.Property')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.State')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='auctions.User')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyImagesUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, upload_to=auctions.models.generate_image_name)),
                ('property_reg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_images', to='auctions.PropertyReg')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyFilesUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(blank=True, upload_to=auctions.models.generate_filename)),
                ('property_reg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_files', to='auctions.PropertyReg')),
            ],
        ),
        migrations.CreateModel(
            name='MakeAnOffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('offer_amount', models.CharField(max_length=10)),
                ('property_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.PropertyReg')),
            ],
        ),
        migrations.AddField(
            model_name='currentauction',
            name='property_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property', to='auctions.PropertyReg'),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.State'),
        ),
        migrations.CreateModel(
            name='BiddingOfProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_bid_amount', models.IntegerField()),
                ('bid_time', models.DateTimeField()),
                ('current_auction_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_bid', to='auctions.CurrentAuction')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_bid', to='auctions.User')),
            ],
        ),
        migrations.AddField(
            model_name='agentuser',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.City'),
        ),
        migrations.AddField(
            model_name='agentuser',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.State'),
        ),
    ]
