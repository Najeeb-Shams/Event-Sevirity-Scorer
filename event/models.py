from django.db import models

class RawEventData(models.Model):
    event_id = models.CharField(max_length=255, unique=True)
    event_link = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    abstract = models.TextField()
    location = models.CharField(max_length=255)
    event_date = models.DateTimeField()
    active = models.BooleanField(default=True)

class Event(models.Model):
    event_id = models.CharField(max_length=255, unique=True)
    # event_link = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    abstract = models.TextField()
    location = models.CharField(max_length=255)
    event_date = models.DateTimeField()
    active = models.BooleanField(default=True)

   
class EventStat(models.Model):
    event_1 = models.ForeignKey(Event, on_delete=models.PROTECT, related_name='+')
    event_2 = models.ForeignKey(Event, on_delete=models.PROTECT, related_name='+')
    event_1_score = models.IntegerField()
    event_2_score = models.IntegerField()
    event_link = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    # updated_at = models.DateTimeField()
    # ranker = models.CharField(max_length=255)

class EventResult(models.Model):
    event_id = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    abstract = models.TextField()
    location = models.CharField(max_length=255)
    event_date = models.DateTimeField()
    # event_link = models.CharField(max_length=255)
    event_severity_score = models.IntegerField()
    created_at = models.DateTimeField()