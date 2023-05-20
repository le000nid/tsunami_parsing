from datetime import datetime

import psycopg2
from requests.exceptions import HTTPError
import requests

conn = psycopg2.connect(database="postgres", user="postgres",
    password="password", host="localhost", port=5432)
cur = conn.cursor()

try:
    response = requests.get('http://www.ioc-sealevelmonitoring.org/ssc/service.php?format=json')
    response.raise_for_status()
    jsonResponse = response.json()

    insert_list = []
    for station in jsonResponse:
        id += 1
        ssc_id = station['ssc_id'] if 'ssc_id' in station.keys() else ""
        name = station['name'] if 'name' in station.keys() else ""
        country = station['country'] if 'country' in station.keys() else ""
        latitude = station['geo:lat'] if 'geo:lat' in station.keys() else 0.0
        longitude = station['geo:lon'] if 'geo:lon' in station.keys() else 0.0

        ioc = station['ioc'] if 'ioc' in station.keys() else []
        if not isinstance(ioc, list):
            ioc = [ioc]
        for i in ioc:
            station_to_insert = (i, name, country, "-", latitude, longitude, "ioc")

        ptwc = station['ptwc'] if 'ptwc' in station.keys() else []
        if not isinstance(ptwc, list):
            ptwc = [ptwc]
        for i in ptwc:
            station_to_insert = (i, name, country, "-", latitude, longitude, "ptwc")
            insert_list.append(station_to_insert)

        gloss = station['gloss'] if 'gloss' in station.keys() else []
        if not isinstance(gloss, list):
            gloss = [gloss]
        for i in gloss:
            station_to_insert = (i, name, country, "-", latitude, longitude, "gloss")
            insert_list.append(station_to_insert)

        uhslc = station['uhslc'] if 'uhslc' in station.keys() else []
        if not isinstance(uhslc, list):
            uhslc = [uhslc]
        for i in uhslc:
            station_to_insert = (i, name, country, "-", latitude, longitude, "uhslc")
            insert_list.append(station_to_insert)

        psmsl = station['psmsl'] if 'psmsl' in station.keys() else []
        if not isinstance(psmsl, list):
            psmsl = [psmsl]
        for i in psmsl:
            station_to_insert = (i, name, country, "-", latitude, longitude, "psmsl")
            insert_list.append(station_to_insert)

        sonel_gps = station['sonel_gps'] if 'sonel_gps' in station.keys() else []
        if not isinstance(sonel_gps, list):
            sonel_gps = [sonel_gps]
        for i in sonel_gps:
            station_to_insert = (i, name, country, "-", latitude, longitude, "sonel_gps")
            insert_list.append(station_to_insert)

        sonel_tg = station['sonel_tg'] if 'sonel_tg' in station.keys() else []
        if not isinstance(sonel_tg, list):
            sonel_tg = [sonel_tg]
        for i in sonel_tg:
            station_to_insert = (i, name, country, "-", latitude, longitude, "sonel_tg")
            insert_list.append(station_to_insert)

    cur.executemany("INSERT INTO stations(station_id,name,country,state,latitude,longitude,source) VALUES(%s,%s,%s,%s,%s,%s,%s)", insert_list)



except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')

conn.commit()
cur.close()

conn.close()