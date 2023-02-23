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
    active_events = list(RawEventData.objects.filter(active=True))
    return sample(active_events, 2)

# def create_events():


def rank_events(request):
    # store_excel_data()
    random_events = []
    event_dict = {}
    #if request.POST and 'ranker' in request.session and not request.POST.get('txtHSelectedEvent') == 're-evaluate':
     #   return render(request, 'rank_submitted.html')
    # store_excel_data()
    current_active_events = list(Event.objects.filter(active=True))
    current_eventstat_events = list(EventStat.objects.filter(Q(event_1__in=current_active_events) | Q(event_2__in=current_active_events)))
    current_eventstat_count = len(current_eventstat_events) if current_active_events else 3

    if current_eventstat_count > 2:
        if current_active_events:
            rank_1_sum = EventStat.objects.filter(event_1_id = current_active_events[0].id).aggregate(Sum('event_1_score')).get('event_1_score__sum')
            rank_2_sum = EventStat.objects.filter(event_2_id = current_active_events[1].id).aggregate(Sum('event_2_score')).get('event_2_score__sum')
            for i, active_event in enumerate(current_active_events):
                score_sum = rank_1_sum if i == 0 else rank_2_sum
                EventResult.objects.create(
                        event_id = active_event.event_id,
                        title = active_event.title,
                        abstract = active_event.abstract,
                        location = active_event.location,
                        event_date = active_event.event_date,
                        event_severity_score = score_sum,
                        # event_link = str(current_active_events[0].event_id)+'-'+str(current_active_events[1].event_id),
                        created_at = timezone.now(),
                        # updated_at = timezone.now()
                    )
        if request.session.get('ranker'):
            del request.session['ranker']
            
        random_events = get_random_events()
        flag_active = True
        for event in random_events:
            raw_event = RawEventData.objects.get(event_id=event.event_id)
            raw_event.active = False
            raw_event.save()

            if not Event.objects.filter(event_id=event.event_id).exists():
                if flag_active:
                    Event.objects.update(active=False)
                    flag_active = False
                event = Event.objects.create(
                        event_id = event.event_id,
                        # event_link = event.event_link,
                        title = event.title,
                        abstract = event.abstract,
                        location = event.location,
                        event_date = event.event_date,
                        active = True
                    )
                event_dict[event.event_id] = event
    elif current_active_events and current_eventstat_count < 3:
        for event in current_active_events:
            event_dict[event.event_id] = event
    if request.method == 'POST':
       # if request.POST.get('txtHSelectedEvent') == 're-evaluate':
         #   return render(request, 'rank_events.html', {'events': event_dict})

        request.session['ranker'] = 'event_ranker'
        print("\n\n", request.session['ranker'])
        # selected_event = current_active_events[0] if current_active_events[0].event_id == request.POST.get('txtHSelectedEvent') else current_active_events[1]
        EventStat.objects.create(
                event_1 = current_active_events[0],
                event_2 = current_active_events[1],
                # ranker = 'abc',
                event_1_score = int(request.POST.get(current_active_events[0].event_id)),
                event_2_score = int(request.POST.get(current_active_events[1].event_id)),
                event_link = str(current_active_events[0].event_id)+'-'+str(current_active_events[1].event_id),
                created_at = timezone.now(),
                # updated_at = timezone.now()
            )

        return render(request, 'rank_submit.html')

    return render(request, 'rank_events.html', {'events': event_dict})

def event_result(request):
    data = EventResult.objects.all()
    return render(request, 'event_status.html', {'data': data})

