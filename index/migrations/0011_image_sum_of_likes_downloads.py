# Generated by Django 2.0.4 on 2018-04-17 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0010_auto_20180416_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='sum_of_likes_downloads',
            field=models.IntegerField(default=0),
        ),
    ]
