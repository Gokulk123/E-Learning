# Generated by Django 3.0.4 on 2020-05-06 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0008_admindata'),
    ]

    operations = [
        migrations.CreateModel(
            name='courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='materials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materials', models.CharField(max_length=100)),
                ('course_id', models.CharField(max_length=100)),
            ],
        ),
    ]