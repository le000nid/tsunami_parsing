import psycopg2
from requests.exceptions import HTTPError
import requests


conn = psycopg2.connect(database="postgres", user="postgres",
                        password="password", host="localhost", port=5432)
cur = conn.cursor()

try:
    response = requests.get(
        'https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations.json?type=waterlevels&units=metric')
    response.raise_for_status()
    jsonResponse = response.json()

    insert_list = []
    for station in jsonResponse["stations"]:
        station_id = station['id'] if 'id' in station.keys() else ""
        name = station['name'] if 'name' in station.keys() else ""
        state = station['state'] if 'state' in station.keys() else ""
        lat = station['lat'] if 'lat' in station.keys() else 0.0
        lng = station['lng'] if 'lng' in station.keys() else 0.0
        station_to_insert = (station_id, name, "America", state, lat, lng, "coops")
        insert_list.append(station_to_insert)
    cur.executemany("INSERT INTO stations(station_id,name,country,state,latitude,longitude,source) VALUES(%s,%s,%s,%s,%s,%s,%s)", insert_list)



except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')

conn.commit()
cur.close()

conn.close()
