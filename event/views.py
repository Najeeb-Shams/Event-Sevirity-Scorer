from django.utils import timezone
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Count, Sum, Q
from .models import Event, EventStat, RawEventData, EventResult
from .data import events_data as data
import openpyxl, os
from datetime import datetime
from random import sample 


APP_PATH = os.path.abspath(os.path.dirname(__file__))
CURRENT_ACTIVE_IDS = []

def load_excel_data_to_db(self):
    if len(list(RawEventData.objects.all())):
        return redirect('/event/rank_events/')

    wb = openpyxl.load_workbook(os.path.join(APP_PATH, 'data/query_result.xlsx'))
    worksheet = wb["Sheet1"]

    row_count = -1
    for row in worksheet.iter_rows():
        row_count += 1
        if row_count == 0:
            continue
        RawEventData.objects.create(
                    event_id = str(row[0].value),
                    event_link = str(row[1].value),
                    title = str(row[2].value),
                    abstract = str(row[3].value),
                    location = str(row[4].value),
                    event_date = datetime.strptime(str(row[5].value), '%Y-%m-%dT%H:%M:%S')
                )
    return redirect('/event/rank_events/')

def get_random_events():
    rank_events = EventStat.objects.filter()
    # queryset = (EventStat.objects.values().filter(is_staff=True,).annotate(total=Count('id'),).order_by('is_staff','total',))
    active_events = list(RawEventData.objects.filter(active=True))
    if not any(active_events):
        return False
    # active_b_events = list(RawEventData.objects.filter(active=True, event_id__startswith='b'))
    return sample(active_events, 2)

def create_events():
    current_active_events = []
    random_events = get_random_events()
    if not random_events:
        return False
    for event in random_events:
        raw_event = RawEventData.objects.get(event_id=event.event_id)
        raw_event.active = False
        raw_event.save()

        if not Event.objects.filter(event_id=event.event_id).exists():
            event = Event.objects.create(
                    event_id = event.event_id,
                    # event_link = event.event_link,
                    title = event.title,
                    abstract = event.abstract,
                    location = event.location,
                    event_date = event.event_date,
                    active = True,
                    event_link = str(random_events[0].event_id)+'-'+str(random_events[1].event_id)
                )
            current_active_events.append(event)
    global CURRENT_ACTIVE_IDS
    CURRENT_ACTIVE_IDS = current_active_events
    return current_active_events


def rank_events(request):
    events_to_rank = []
    events_to_result = []
    event_dict = {}
    all_eventstat_total = list(EventStat.objects.values('event_link').annotate(total=Count('event_link')).order_by())
    for stat in all_eventstat_total:
        if stat.get('total') < 3:
            events_to_rank.append(stat)
        elif stat.get('total') == 3:
            event_ids = [int(link) for link in stat.get('event_link').split('-')]
            to_check_event_ids = [event for event in Event.objects.filter(event_id__in=event_ids)]
            if to_check_event_ids[0].active:
                events_to_result.append(stat)
    global CURRENT_ACTIVE_IDS
    if not 'ranker' in request.session and request.method != 'POST':
        if events_to_rank:
            current_event_ids = [int(link) for link in events_to_rank[0].get('event_link').split('-')]
            current_active_events = [event for event in Event.objects.filter(event_id__in=current_event_ids)]
            CURRENT_ACTIVE_IDS = current_active_events
        else:
            current_active_events = create_events()
            if not current_active_events:
                return render(request, 'event_completed.html')
    elif 'ranker' in request.session and request.method != 'POST':
        current_active_events = create_events()
        if not current_active_events:
                return render(request, 'event_completed.html')
    else:
        current_active_events = CURRENT_ACTIVE_IDS
    if events_to_result:
        event_to_result_ids = [int(link) for link in events_to_result[0].get('event_link').split('-')]
        current_to_result_events = [event for event in Event.objects.filter(event_id__in=event_to_result_ids).filter(active=True)]
        if current_to_result_events:
            rank_1_sum = EventStat.objects.filter(event_1_id = current_to_result_events[0].id).aggregate(Sum('event_1_score')).get('event_1_score__sum')
            rank_2_sum = EventStat.objects.filter(event_2_id = current_to_result_events[1].id).aggregate(Sum('event_2_score')).get('event_2_score__sum')

            for i, active_event in enumerate(current_to_result_events):
                score_sum = rank_1_sum if i == 0 else rank_2_sum
                EventResult.objects.create(
                        event_id = active_event.event_id,
                        title = active_event.title,
                        abstract = active_event.abstract,
                        location = active_event.location,
                        event_date = active_event.event_date,
                        event_severity_score = score_sum,
                        created_at = timezone.now(),
                    )
                active_event.active = False
                active_event.save()

    for event in current_active_events:
        event_dict[event.event_id] = event
    if request.method == 'POST':
        if request.POST.get('txtHSelectedEvent') == 're-evaluate':
            return render(request, 'rank_events.html', {'events': event_dict})
             
            

        request.session['ranker'] = 'event_ranker'
        EventStat.objects.create(
                event_1 = current_active_events[0],
                event_2 = current_active_events[1],
                event_1_score = int(request.POST.get(current_active_events[0].event_id)),
                event_2_score = int(request.POST.get(current_active_events[1].event_id)),
                event_link = str(current_active_events[0].event_id)+'-'+str(current_active_events[1].event_id),
                created_at = timezone.now(),
            )

        return render(request, 'rank_submit.html')

    # return render(request, 'rank_events.html', {'events': event_dict})

# this line is only for temporary stop, for resumming the services the above line should be uncomment
    return render(request, 'stopped.html', {'events': event_dict})

def event_result(request):
    data = EventResult.objects.all()
    return render(request, 'event_status.html', {'data': data})
