from django.shortcuts import render
from  . sparql import events_list

def events_view(request):
   mynam={"name":"Najeeb", "lname":"Shams"}
   return render(request, 'events.html',events_list)
    

# test function
def hi(request):
   # A dictionary containing data that will be passed to the template
    context = {'key':'Hi there! from "hi" test funciton'} 
    return render(request, "hi.html", context)
