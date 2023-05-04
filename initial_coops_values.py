from datetime import datetime

import psycopg2
from requests.exceptions import HTTPError
import requests

conn = psycopg2.connect(database="postgres", user="postgres",
                        password="password", host="localhost", port=5432)
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS coops_station_values")
cur.execute("CREATE TABLE coops_station_values (id SERIAL PRIMARY KEY, " +
            "station_id INTEGER, t VARCHAR(64), v VARCHAR(64), s VARCHAR(64), f VARCHAR(64), q VARCHAR(64), CONSTRAINT fk_station FOREIGN KEY(station_id) REFERENCES coops_stations(id))")

try:
    cur.execute("SELECT id FROM coops_stations")
    ids = cur.fetchall()

    insert_list = []
    id = 0
    for station in ids:
        response = requests.get(
            'https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?date=recent&station=' + str(station[0]) + '&product=water_level&datum=STND&time_zone=gmt&units=english&format=json')
        response.raise_for_status()
        jsonResponse = response.json()
        if 'data' in jsonResponse.keys():
            for value in jsonResponse['data']:
                station_id = station[0]
                t = value['t'] if 't' in value.keys() else ""
                v = value['v'] if 'v' in value.keys() else ""
                s = value['s'] if 's' in value.keys() else ""
                f = value['f'] if 'f' in value.keys() else ""
                q = value['q'] if 'q' in value.keys() else ""
                station_to_insert = (id, station_id, t, v, s, f, q)
                id += 1
                insert_list.append(station_to_insert)
    cur.executemany("INSERT INTO coops_station_values VALUES(%s,%s,%s,%s,%s,%s,%s)", insert_list)



except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')

conn.commit()
cur.close()

conn.close()
