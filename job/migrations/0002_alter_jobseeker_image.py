# Generated by Django 5.0.2 on 2024-03-23 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobseeker',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='user'),
        ),
    ]
