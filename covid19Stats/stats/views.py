from django.views.generic import DetailView, ListView
from django.shortcuts import render
from django.db.models import Sum
from .models import Stats


class DashboardView(ListView):
    model = Stats
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_stats_object = Stats.objects.get(country='All')
        context['total_cases'] = all_stats_object.total_cases
        context['total_deaths'] = all_stats_object.total_deaths
        context['recovered_cases'] = all_stats_object.recovered_cases

        return context
    
class MapView(ListView):
    model = Stats
    template_name = 'map.html'