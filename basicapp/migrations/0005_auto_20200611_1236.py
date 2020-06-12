# Generated by Django 3.0.3 on 2020-06-11 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0004_contact_us_feed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookings',
            name='slot',
        ),
        migrations.AddField(
            model_name='bookings',
            name='check',
            field=models.CharField(default=0, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookings',
            name='cht',
            field=models.CharField(default=0, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookings',
            name='date',
            field=models.CharField(default=0, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookings',
            name='end',
            field=models.CharField(default=0, max_length=40),
            preserve_default=False,
        ),
    ]
