from datetime import datetime

import psycopg2
from requests.exceptions import HTTPError
import requests

conn = psycopg2.connect(database="postgres", user="postgres",
                        password="password", host="localhost", port=5432)
cur = conn.cursor()

try:
    cur.execute("SELECT id, station_id FROM stations WHERE source='coops'")
    ids = cur.fetchall()

    insert_list = []
    for station in ids:
        response = requests.get(
            'https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?date=recent&station=' + str(station[1]) + '&product=water_level&datum=STND&time_zone=gmt&units=english&format=json')
        response.raise_for_status()
        jsonResponse = response.json()
        if 'data' in jsonResponse.keys():
            for value in jsonResponse['data']:
                time_str = value['t'] if 't' in value.keys() else ""
                time = datetime(time_str[0:4], time_str[5:7], time_str[8:10], time_str[11:13], time_str[14:16])
                v = value['v'] if 'v' in value.keys() else ""
                station_to_insert = (station[0], time, v, 'STND')
                insert_list.append(station_to_insert)
    cur.executemany("INSERT INTO station_values(station_id, time, value, datum) VALUES(%s,%s,%s,%s)", insert_list)



except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')

conn.commit()
cur.close()

conn.close()
