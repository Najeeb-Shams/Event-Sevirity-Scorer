from django.urls import path
from . import views

urlpatterns = [
    # the follwoing two test samples are the same
    path ('hi/', views.hi, name="Hello"), 
    # path ('hi/', views.hi, 'Hello'),
    path ('events/', views.events_view , name='events_view'),
    
]