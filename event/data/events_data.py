from datetime import datetime
from django.utils import timezone

events = {
    'events': [
        {
            'head': 'Event 1',
            'title': 'Event 1 Title',
            'description': 'Here the title will come and the there will alot more stuff regarding the Event 1. All the content here will be stored in database and will disappear auto after some periond of time or the use interaction is completed',
            'id': 1,
            'sub_title': 'The title 1',
            'event_date': timezone.now(),
            'other_info': 'Other info 1',
        },
        {
            'head': 'Event 2',
            'title': 'Event 2 Title',
            'description': 'Here the title will come and the there will alot more stuff regarding the Event 2. All the content here will be stored in database and will disappear auto after some periond of time or the use interaction is completed',
            'id': 2,
            'sub_title': 'The title 2',
            'event_date': timezone.now(),
            'other_info': 'Other info 2',
        },
    ]
}