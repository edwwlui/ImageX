# Generated by Django 2.0.4 on 2018-04-16 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0009_auto_20180416_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='LikedMember',
            field=models.ManyToManyField(related_name='member_liked', to='index.Member'),
        ),
        migrations.AlterField(
            model_name='image',
            name='photographer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='member_photographer', to='index.Member'),
        ),
    ]
