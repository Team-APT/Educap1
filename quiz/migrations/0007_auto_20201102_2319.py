# Generated by Django 3.1.2 on 2020-11-02 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_auto_20201102_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlistwishlistitem',
            name='user',
            field=models.CharField(max_length=30),
        ),
    ]
