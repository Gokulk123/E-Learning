# Generated by Django 3.0.4 on 2020-03-30 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0003_auto_20200330_1335'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='userdetails',
            new_name='users',
        ),
    ]