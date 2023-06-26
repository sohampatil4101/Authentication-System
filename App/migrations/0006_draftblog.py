# Generated by Django 4.1.5 on 2023-06-25 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_createblog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Draftblog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('image', models.FileField(default=0, upload_to='images/')),
                ('category', models.TextField(choices=[('Mental Health', 'Mental Health'), ('Heart Disease', 'Heart Disease'), ('Covid19', 'Covid19'), ('Immunization', 'Immunization ')], default='Mental Health')),
                ('summary', models.TextField()),
                ('content', models.TextField()),
            ],
        ),
    ]
