import requests
from requests.exceptions import HTTPError
import csv


try:
    response = requests.get('https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations.json?type=waterlevels&units=metric')
    response.raise_for_status()
    # access JSOn content
    jsonResponse = response.json()

    print("Entire JSON response")
    print(jsonResponse['stations'])

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')