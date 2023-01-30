from django.urls import path
from . import views

urlpatterns = [
    path ('hi/', views.hi, name="Hello"), 
    path ('events/', views.events_view , name='events_view'),
    
]
