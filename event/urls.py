from django.urls import path
from . import views


urlpatterns = [
    path('rank_events/', views.rank_events),
    path('event_result/', views.event_result),
    path('load_data/', views.load_excel_data_to_db),
]