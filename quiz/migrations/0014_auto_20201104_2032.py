# Generated by Django 3.1.2 on 2020-11-04 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0013_phoneconsult'),
    ]

    operations = [
        migrations.AddField(
            model_name='collegesofcourse',
            name='rating',
            field=models.CharField(default='2.75/5', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collegesofcourse',
            name='site',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
