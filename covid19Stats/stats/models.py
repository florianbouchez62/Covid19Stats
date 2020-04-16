from django.db import models


class Stats(models.Model):
    country = models.TextField("country", primary_key=True)
    new_cases = models.TextField("new_cases", null=True)
    active_cases = models.IntegerField("active_cases", null=True)
    critical_cases = models.IntegerField("critical_cases", null=True)
    recovered_cases = models.IntegerField("recovered_cases", null=True)
    total_cases = models.IntegerField("total_cases", null=True)
    new_deaths = models.TextField('new_deaths', null=True)
    total_deaths = models.IntegerField("total_deaths", null=True)
    total_tests = models.IntegerField("total_tests", null=True)
    day = models.TextField("day")
    time = models.TextField("time")
    type_stat = models.TextField("type_stat")