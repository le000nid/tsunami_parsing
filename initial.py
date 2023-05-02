from datetime import datetime

import psycopg2
from requests.exceptions import HTTPError
import requests

conn = psycopg2.connect(database="postgres", user="postgres",
    password="4816", host="localhost", port=5432)
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS unesco_stations")
cur.execute("CREATE TABLE unesco_stations (id SERIAL PRIMARY KEY, " +
    "ssc_id VARCHAR(64), name VARCHAR(64), country VARCHAR(64), latitude DOUBLE PRECISION, longitude DOUBLE PRECISION, " +
            "ioc VARCHAR(64) ARRAY, ptwc VARCHAR(64) ARRAY, gloss VARCHAR(64) ARRAY, uhslc VARCHAR(64) ARRAY, " +
            "psmsl VARCHAR(64) ARRAY, sonel_gps VARCHAR(64) ARRAY, sonel_tg VARCHAR(64) ARRAY, modified TIMESTAMP(0))")

try:
    response = requests.get('http://www.ioc-sealevelmonitoring.org/ssc/service.php?format=json')
    response.raise_for_status()
    jsonResponse = response.json()

    insert_list = []
    id = 0
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
        ptwc = station['ptwc'] if 'ptwc' in station.keys() else []
        if not isinstance(ptwc, list):
            ptwc = [ptwc]
        gloss = station['gloss'] if 'gloss' in station.keys() else []
        if not isinstance(gloss, list):
            gloss = [gloss]
        uhslc = station['uhslc'] if 'uhslc' in station.keys() else []
        if not isinstance(uhslc, list):
            uhslc = [uhslc]
        psmsl = station['psmsl'] if 'psmsl' in station.keys() else []
        if not isinstance(psmsl, list):
            psmsl = [psmsl]
        sonel_gps = station['sonel_gps'] if 'sonel_gps' in station.keys() else []
        if not isinstance(sonel_gps, list):
            sonel_gps = [sonel_gps]
        sonel_tg = station['sonel_tg'] if 'sonel_tg' in station.keys() else []
        if not isinstance(sonel_tg, list):
            sonel_tg = [sonel_tg]
        modified = datetime(int(station['dcterms:modified'][:4]), int(station['dcterms:modified'][5:7]), int(station['dcterms:modified'][8:10]), int(station['dcterms:modified'][11:13]), int(station['dcterms:modified'][14:16]), int(station['dcterms:modified'][17:19])) if 'dcterms:modified' in station.keys() else datetime.min
        station_to_insert = (id, ssc_id, name, country, latitude, longitude, ioc, ptwc, gloss, uhslc, psmsl, sonel_gps, sonel_tg, modified)
        id += 1
        insert_list.append(station_to_insert)
    cur.executemany("INSERT INTO unesco_stations VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", insert_list)



except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')

conn.commit()
cur.close()

conn.close()