# Generated by Django 3.0.6 on 2020-05-06 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0002_auto_20200506_2354'),
    ]

    operations = [
        migrations.AddField(
            model_name='meals',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
