# Generated by Django 3.0.4 on 2020-05-06 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0009_courses_materials'),
    ]

    operations = [
        migrations.CreateModel(
            name='assign_work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty', models.CharField(max_length=100)),
                ('course_id', models.CharField(max_length=100)),
            ],
        ),
    ]