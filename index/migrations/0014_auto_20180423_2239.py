# Generated by Django 2.0.3 on 2018-04-23 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0013_auto_20180423_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='LikedMember',
            field=models.ManyToManyField(blank=True, related_name='member_liked', to='index.Member'),
        ),
    ]
