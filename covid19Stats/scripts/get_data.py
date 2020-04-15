import http.client
import json
import sqlite3
import os
from stats.models import Stats

def run():

    conn = http.client.HTTPSConnection("covid-193.p.rapidapi.com")

    headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "5bffb4691cmsh45cb38845097bccp12c2ddjsn51a0858f137f"
    }

    conn.request("GET", "/countries", headers=headers)

    res = conn.getresponse()
    data = res.read().decode('utf8')

    countries = json.loads(data)['response']

    conn.request("GET", "/statistics", headers=headers)

    res = conn.getresponse()
    data = res.read().decode('utf8')

    entries = json.loads(data)['response']

    for row in entries:
        row_object = Stats.objects.filter(country=row['country'])
        if row_object:
            row_object.delete()
        if row['country'] in countries:
            Stats.objects.create(
                country = row['country'],
                new_cases = row['cases']['new'],
                active_cases = row['cases']['active'],
                critical_cases = row['cases']['critical'],
                recovered_cases = row['cases']['recovered'],
                total_cases = row['cases']['total'],
                new_deaths = row['deaths']['new'],
                total_deaths = row['deaths']['total'],
                total_tests = row['tests']['total'],
                day = row['day'],
                time = row['time']
        )