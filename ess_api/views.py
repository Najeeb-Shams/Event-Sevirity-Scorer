from django.shortcuts import render
from  . sparql import events_list

def events_view(request):
     return render(request, 'events.html',events_list)
    
