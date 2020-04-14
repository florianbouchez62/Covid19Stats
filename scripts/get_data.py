import http.client
import json
import sqlite3
import os


def create_stats_if_not_exists(c):
    c.execute("CREATE TABLE IF NOT EXISTS stats ("
              "country TEXT PRIMARY KEY,"
              "new_cases TEXT,"
              "active_cases NUMBER,"
              "critical_cases NUMBER,"
              "recovered_cases NUMBER,"
              "total_cases NUMBER,"
              "new_deaths TEXT,"
              "total_deaths NUMBER,"
              "total_tests NUMBER,"
              "day TEXT,"
              "time TEXT)")


def insert_stat(stat, c, cnx):
    country = row['country']
    new_cases = row['cases']['new']
    active_cases = row['cases']['active']
    critical_cases = row['cases']['critical']
    recovered_cases = row['cases']['recovered']
    total_cases = row['cases']['total']
    new_deaths = row['deaths']['new']
    total_deaths = row['deaths']['total']
    total_tests = row['tests']['total']
    day = row['day']
    time = row['time']
    params = (country, new_cases, active_cases, critical_cases, recovered_cases, total_cases, new_deaths, total_deaths,
              total_tests, day, time,)
    c.execute("INSERT INTO stats VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", params)


def delete_stat(country, c, cnx):
    c.execute("DELETE FROM stats WHERE country = ?", (country,))
    cnx.commit()


path = os.path.dirname(os.path.abspath(__file__))[:-7]
db_conn = sqlite3.connect(path + 'database/stats.db')
cursor = db_conn.cursor()
create_stats_if_not_exists(cursor)

conn = http.client.HTTPSConnection("covid-193.p.rapidapi.com")

headers = {
  'x-rapidapi-host': "covid-193.p.rapidapi.com",
  'x-rapidapi-key': "5bffb4691cmsh45cb38845097bccp12c2ddjsn51a0858f137f"
}

conn.request("GET", "/statistics", headers=headers)

res = conn.getresponse()
data = res.read().decode('utf8')

entries = json.loads(data)['response']

for row in entries:
    delete_stat(row['country'], cursor, db_conn)
    insert_stat(row, cursor, db_conn)

db_conn.close()
