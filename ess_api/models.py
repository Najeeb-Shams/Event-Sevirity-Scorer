# Create your models here.
# from django.db import models
# import pandas as pd
# from django.db import IntegrityError
# from .models import Event

# class Event(models.Model):
#     event_id = models.CharField(max_length=255, unique=True)
#     event_title = models.CharField(max_length=255)
#     event_details = models.TextField()
#     event_location = models.CharField(max_length=255)


   

# # read the csv file
# df = pd.read_csv("https://github.com/semantic-systems/coypu-wiki-events")

# #iterating through rows of the dataframe
# for index, row in df.iterrows():
#     try:
#         event = Event(event_id=row['event_id'], event_title=row['event_title'], event_details=row['event_details'], event_location=row['event_location'])
#         event.save()
#     except IntegrityError:
#         pass
