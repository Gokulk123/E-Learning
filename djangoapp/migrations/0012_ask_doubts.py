# Generated by Django 3.0.4 on 2020-05-07 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0011_courses_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='ask_doubts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_id', models.CharField(max_length=100)),
                ('course_name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('question', models.CharField(max_length=100)),
            ],
        ),
    ]
