# Generated by Django 3.0.6 on 2020-05-06 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contributors', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createcontributor',
            name='role',
        ),
    ]
