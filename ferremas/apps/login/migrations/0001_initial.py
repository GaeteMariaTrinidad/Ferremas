# Generated by Django 5.0.6 on 2024-06-27 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('contrasena', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=100)),
            ],
        ),
    ]