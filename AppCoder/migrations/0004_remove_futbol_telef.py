# Generated by Django 4.1.3 on 2022-12-19 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0003_futbol'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='futbol',
            name='telef',
        ),
    ]
