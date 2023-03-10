# Generated by Django 4.1.6 on 2023-02-13 05:57

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_raweventdata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='description',
        ),
        migrations.RemoveField(
            model_name='event',
            name='head',
        ),
        migrations.RemoveField(
            model_name='event',
            name='other_info',
        ),
        migrations.RemoveField(
            model_name='event',
            name='sub_title',
        ),
        migrations.AddField(
            model_name='event',
            name='abstract',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='event_link',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(default=datetime.datetime(2023, 2, 13, 5, 57, 0, 12509, tzinfo=datetime.timezone.utc), max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_id',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='raweventdata',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
