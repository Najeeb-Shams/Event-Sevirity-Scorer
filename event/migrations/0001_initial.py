# Generated by Django 4.1.7 on 2023-03-31 02:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.CharField(max_length=255, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('abstract', models.TextField()),
                ('location', models.CharField(max_length=255)),
                ('event_date', models.DateTimeField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.CharField(max_length=255, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('abstract', models.TextField()),
                ('location', models.CharField(max_length=255)),
                ('event_date', models.DateTimeField()),
                ('event_severity_score', models.IntegerField()),
                ('created_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='RawEventData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.CharField(max_length=255, unique=True)),
                ('event_link', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('abstract', models.TextField()),
                ('location', models.CharField(max_length=255)),
                ('event_date', models.DateTimeField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventStat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_1_score', models.IntegerField()),
                ('event_2_score', models.IntegerField()),
                ('event_link', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField()),
                ('event_1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='event.event')),
                ('event_2', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='event.event')),
            ],
        ),
    ]