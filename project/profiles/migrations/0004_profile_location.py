# Generated by Django 3.0.5 on 2020-04-16 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20200416_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(default='my location', max_length=120),
        ),
    ]
