# Generated by Django 3.0.6 on 2020-05-09 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0003_meals_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
    ]
