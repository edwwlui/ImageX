# Generated by Django 2.0.4 on 2018-04-16 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20180416_0114'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('ABS', 'Abstract'), ('AER', 'Aerial'), ('ANI', 'Animals'), ('ARC', 'Architecture'), ('BNW', 'Black and White'), ('FAM', 'Family'), ('FAS', 'Fashion'), ('FIA', 'Fine Art'), ('FOO', 'Food'), ('JOU', 'Journalism'), ('LAN', 'Landscape'), ('MAC', 'Macro'), ('NAT', 'Nature'), ('NIG', 'Night'), ('PEO', 'People'), ('PEA', 'Performing Arts'), ('SPO', 'Sport'), ('STL', 'Still Life'), ('STR', 'Street'), ('TRA', 'Travel')], max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='gallery',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='index.Category'),
        ),
        migrations.AlterField(
            model_name='image',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='index.Category'),
        ),
    ]
