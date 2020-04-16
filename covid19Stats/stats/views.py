from django.views.generic import DetailView, ListView
from django.shortcuts import render
from django.db.models import Sum
from .models import Stats
from datetime import datetime
import json


class DashboardView(ListView):
    model = Stats
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_stats_object = Stats.objects.filter(type_stat="country")
        distribution_continents = Stats.objects.filter(type_stat="continent")
        time = datetime.strptime(all_stats_object[:1].get().time, "%Y-%m-%dT%H:%M:%S%z")
        top_total_cases = all_stats_object.order_by('-total_cases').values_list('total_cases', flat=True).distinct()
        top_records = all_stats_object.order_by('-total_cases').filter(total_cases__in=top_total_cases[:5])
        context['all_stats'] = all_stats_object.order_by('-total_cases')
        context['total_cases'] = all_stats_object.aggregate(Sum('total_cases'))
        context['total_deaths'] = all_stats_object.aggregate(Sum('total_deaths'))
        context['recovered_cases'] = all_stats_object.aggregate(Sum('recovered_cases'))
        context['time'] = time.strftime("%Y/%m/%d %H:%M:%S")
        context['top_countries'] = json.dumps([ record.country for record in top_records])
        context['top_total_cases'] = json.dumps([ record.total_cases for record in top_records])
        context['continents_name'] = json.dumps([continent.country for continent in distribution_continents])
        context['continents_total_cases'] = json.dumps([continent.total_cases for continent in distribution_continents])
        context['continents_total_deaths'] = json.dumps([continent.total_deaths for continent in distribution_continents])
        context['continents_total_recovered'] = json.dumps([continent.recovered_cases for continent in distribution_continents])

        for i in all_stats_object:
            print(i)

        return context
    
class MapView(ListView):
    model = Stats
    template_name = 'map.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_stats_object = Stats.objects.get(country='France')
        time = datetime.strptime(all_stats_object.time, "%Y-%m-%dT%H:%M:%S%z")
        context['all_objects'] = json.dumps([[obj.country, obj.total_cases, obj.total_deaths] for obj in Stats.objects.all()])
        context['time'] = time.strftime("%Y/%m/%d %H:%M:%S")

        return context
    