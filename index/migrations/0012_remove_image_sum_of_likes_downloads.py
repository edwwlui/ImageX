# Generated by Django 2.0.3 on 2018-04-23 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0011_image_sum_of_likes_downloads'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='sum_of_likes_downloads',
        ),
    ]