# Generated by Django 4.1.3 on 2022-12-19 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_rename_numero_comision_curso_comision_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Futbol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('apellido', models.CharField(max_length=60)),
                ('anio_nacimiento', models.IntegerField()),
                ('telef', models.IntegerField()),
            ],
        ),
    ]
