# Generated by Django 3.1.2 on 2020-11-03 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0010_college_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='college',
            name='slug',
        ),
    ]
