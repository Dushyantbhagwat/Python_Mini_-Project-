# Generated by Django 5.0.2 on 2024-03-15 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobseeker',
            name='image',
            field=models.ImageField(null=True, upload_to='job/user_image'),
        ),
    ]
