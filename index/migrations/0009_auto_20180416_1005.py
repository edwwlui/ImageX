# Generated by Django 2.0.4 on 2018-04-16 10:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_auto_20180416_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='avatarImage',
            field=models.ImageField(blank=True, null=True, upload_to='avatar/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg'])]),
        ),
    ]
