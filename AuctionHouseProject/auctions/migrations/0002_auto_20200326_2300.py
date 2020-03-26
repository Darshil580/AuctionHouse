# Generated by Django 3.0.4 on 2020-03-26 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agentuser',
            name='image',
            field=models.ImageField(blank=True, upload_to='agent_image'),
        ),
        migrations.AlterField(
            model_name='agentuser',
            name='proof_document',
            field=models.FileField(blank=True, upload_to='agent_proof_document'),
        ),
        migrations.AlterField(
            model_name='agentuser',
            name='resume_document',
            field=models.FileField(blank=True, upload_to='agent_resume_document'),
        ),
    ]
