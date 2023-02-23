from django.shortcuts import render
from  . sparql import results
# from  . sparql import events_list

# def events_view(request):
#      return render(request, 'events.html',events_list)
    
def events_view(request):
   cards = [
        {'title': 'Card 1', 'description': 'Description for card 1'},
        {'title': 'Card 2', 'description': 'Description for card 2'},
        {'title': 'Card 3', 'description': 'Description for card 3'},
    ]
   return render(request, 'events.html', events_list)


def score_event(request):
   return render(request, 'score_event.html', results)


# test function
def hi(request):
   # A dictionary containing data that will be passed to the template
    context = {'key':'Hi there! from "hi" test funciton'} 
    return render(request, "hi.html", context)