# Generated by Django 4.1.5 on 2023-06-25 04:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_rename_images_doctor_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='pincode',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='pincode',
        ),
    ]
