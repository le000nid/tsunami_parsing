import requests
from requests.exceptions import HTTPError
import csv
import pandas as pd


try:
    response = requests.get('http://www.ioc-sealevelmonitoring.org/ssc/service.php?format=json')
    response.raise_for_status()
    # access JSOn content
    jsonResponse = response.json()

    # df = pd.DataFrame(jsonResponse)
    # df.to_csv("list_of_stations.csv")

    print("Entire JSON response")
    print(jsonResponse)

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')