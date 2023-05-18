from datetime import datetime

import psycopg2
from requests.exceptions import HTTPError
import requests

conn = psycopg2.connect(database="postgres", user="postgres",
                        password="password", host="localhost", port=5432)
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS noaa_tsunamis_events")
cur.execute("CREATE TABLE noaa_tsunamis_events (id SERIAL PRIMARY KEY, " +
            "area VARCHAR(64), assocDeposits VARCHAR(64), country VARCHAR(64), locationName VARCHAR(64), causeCode INTEGER, damageAmountOrder INTEGER, damageAmountOrderTotal INTEGER, damageMillionsDollars INTEGER, damageMillionsDollarsTotal INTEGER, " +
            "day INTEGER, deaths INTEGER, deathsAmountOrder INTEGER, deathsAmountOrderTotal INTEGER, deathsTotal INTEGER, earthquakeEventId INTEGER, " +
            "eventValidity INTEGER, hour INTEGER, housesDamaged INTEGER, housesDamagedAmountOrder INTEGER, housesDamagedAmountOrderTotal INTEGER, housesDamagedTotal INTEGER, " +
            "housesDestroyed INTEGER, housesDestroyedAmountOrder INTEGER, housesDestroyedAmountOrderTotal INTEGER, housesDestroyedTotal INTEGER, injuries INTEGER, injuriesAmountOrder INTEGER, injuriesAmountOrderTotal INTEGER, " +
            "injuriesTotal INTEGER, maxWaterHeight INTEGER, minute INTEGER, missing INTEGER, missingAmountOrder INTEGER, missingAmountOrderTotal INTEGER, missingTotal INTEGER, " +
            "month INTEGER, numDeposits INTEGER, numRunups INTEGER, regionCode INTEGER, second INTEGER, tsIntensity INTEGER, tsMtAbe INTEGER, " +
            "volcanoEventId INTEGER, year INTEGER, warningStatusId INTEGER, publish BOOL, " +
            "latitude DOUBLE PRECISION, longitude DOUBLE PRECISION)")

try:
    response = requests.get('http://www.ngdc.noaa.gov/hazel/hazard-service/api/v1/tsunamis/events')
    # response.raise_for_status()
    # jsonResponse = response.json()
    #
    # insert_list = []
    # for station in jsonResponse["stations"]:
    #     id = station['id'] if 'id' in station.keys() else ""
    #     name = station['name'] if 'name' in station.keys() else ""
    #     state = station['state'] if 'state' in station.keys() else ""
    #     lat = station['lat'] if 'lat' in station.keys() else 0.0
    #     lng = station['lng'] if 'lng' in station.keys() else 0.0
    #     station_to_insert = (id, name, state, lat, lng)
    #     insert_list.append(station_to_insert)
    # cur.executemany("INSERT INTO noaa_tsunamis_events VALUES(%s,%s,%s,%s,%s)", insert_list)



except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')

conn.commit()
cur.close()

conn.close()
