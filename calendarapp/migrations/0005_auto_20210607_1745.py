# Generated by Django 3.0.8 on 2021-06-07 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendarapp', '0004_remove_event_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateField(),
        ),
    ]
