# Generated by Django 3.0.4 on 2020-03-30 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_details',
            name='district',
            field=models.CharField(default='SOME STRING', max_length=50),
        ),
        migrations.AddField(
            model_name='user_details',
            name='hname',
            field=models.CharField(default='SOME STRING', max_length=20),
        ),
        migrations.AddField(
            model_name='user_details',
            name='pincode',
            field=models.CharField(default='SOME STRING', max_length=20),
        ),
        migrations.AddField(
            model_name='user_details',
            name='state',
            field=models.CharField(default='SOME STRING', max_length=20),
        ),
        migrations.AddField(
            model_name='user_details',
            name='street',
            field=models.CharField(default='SOME STRING', max_length=20),
        ),
    ]