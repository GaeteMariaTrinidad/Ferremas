# Generated by Django 5.0.6 on 2024-06-29 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='nombre',
            new_name='nomre',
        ),
    ]
