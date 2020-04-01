# Generated by Django 3.0.4 on 2020-03-31 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertyreg',
            name='city',
            field=models.CharField(default='Place to be Selected.', max_length=30),
        ),
        migrations.AddField(
            model_name='propertyreg',
            name='pincode',
            field=models.CharField(default='000000', max_length=6),
        ),
        migrations.AddField(
            model_name='propertyreg',
            name='state',
            field=models.CharField(default='To be Selected', max_length=30),
        ),
        migrations.AlterField(
            model_name='propertyreg',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='propertyreg',
            name='property_description',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.CreateModel(
            name='PropertyImagesUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, upload_to='property_images')),
                ('property_reg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_images', to='auctions.PropertyReg')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyFilesUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(blank=True, upload_to='property_files')),
                ('property_reg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_files', to='auctions.PropertyReg')),
            ],
        ),
    ]