from django.views.generic import DetailView, ListView
from django.shortcuts import render
from django.db.models import Sum
from .models import Stats
import datetime
import json


class DashboardView(ListView):
    model = Stats
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_stats_object = Stats.objects.get(country='All')
        context['total_cases'] = all_stats_object.total_cases
        context['total_deaths'] = all_stats_object.total_deaths
        context['recovered_cases'] = all_stats_object.recovered_cases
        time = datetime.datetime.strptime(all_stats_object.time, "%Y-%m-%dT%H:%M:%S%z")
        context['time'] = time.strftime("%Y/%m/%d %H:%M:%S")

        return context
    
class MapView(ListView):
    model = Stats
    template_name = 'map.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_stats_object = Stats.objects.get(country='France')
        context['all_objects'] = json.dumps([[obj.country, obj.total_cases, obj.total_deaths] for obj in Stats.objects.all()])
        time = datetime.datetime.strptime(all_stats_object.time, "%Y-%m-%dT%H:%M:%S%z")
        context['time'] = time.strftime("%Y/%m/%d %H:%M:%S")
        return context
    