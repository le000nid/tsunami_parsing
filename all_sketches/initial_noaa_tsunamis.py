from datetime import datetime

import psycopg2
from requests.exceptions import HTTPError
import requests

conn = psycopg2.connect(database="postgres", user="postgres",
                        password="password", host="localhost", port=5432)
cur = conn.cursor()

try:
    response = requests.get('http://www.ngdc.noaa.gov/hazel/hazard-service/api/v1/tsunamis/events')
    response.raise_for_status()
    jsonResponse = response.json()

    insert_list = []
    for tsunami in jsonResponse["items"]:
        noaa_id = tsunami['id'] if 'id' in tsunami.keys() else 0
        area = tsunami['area'] if 'area' in tsunami.keys() else ""
        assocDeposits = tsunami['assocDeposits'] if 'assocDeposits' in tsunami.keys() else ""
        country = tsunami['country'] if 'country' in tsunami.keys() else ""
        locationName = tsunami['locationName'] if 'locationName' in tsunami.keys() else ""
        causeCode = tsunami['causeCode'] if 'causeCode' in tsunami.keys() else 0
        damageAmountOrder = tsunami['damageAmountOrder'] if 'damageAmountOrder' in tsunami.keys() else 0
        damageAmountOrderTotal = tsunami['damageAmountOrderTotal'] if 'damageAmountOrderTotal' in tsunami.keys() else 0
        damageMillionsDollars = tsunami['damageMillionsDollars'] if 'damageMillionsDollars' in tsunami.keys() else 0
        damageMillionsDollarsTotal = tsunami[
            'damageMillionsDollarsTotal'] if 'damageMillionsDollarsTotal' in tsunami.keys() else 0
        day = tsunami['day'] if 'day' in tsunami.keys() else 0
        deaths = tsunami['deaths'] if 'deaths' in tsunami.keys() else 0
        deathsAmountOrder = tsunami['deathsAmountOrder'] if 'deathsAmountOrder' in tsunami.keys() else 0
        deathsAmountOrderTotal = tsunami['deathsAmountOrderTotal'] if 'deathsAmountOrderTotal' in tsunami.keys() else 0
        deathsTotal = tsunami['deathsTotal'] if 'deathsTotal' in tsunami.keys() else 0
        earthquakeEventId = tsunami['earthquakeEventId'] if 'earthquakeEventId' in tsunami.keys() else 0
        eventValidity = tsunami['eventValidity'] if 'eventValidity' in tsunami.keys() else 0
        hour = tsunami['hour'] if 'hour' in tsunami.keys() else 0
        housesDamaged = tsunami['housesDamaged'] if 'housesDamaged' in tsunami.keys() else 0
        housesDamagedAmountOrder = tsunami[
            'housesDamagedAmountOrder'] if 'housesDamagedAmountOrder' in tsunami.keys() else 0
        housesDamagedAmountOrderTotal = tsunami[
            'housesDamagedAmountOrderTotal'] if 'housesDamagedAmountOrderTotal' in tsunami.keys() else 0
        housesDamagedTotal = tsunami['housesDamagedTotal'] if 'housesDamagedTotal' in tsunami.keys() else 0
        housesDestroyed = tsunami['housesDestroyed'] if 'housesDestroyed' in tsunami.keys() else 0
        housesDestroyedAmountOrder = tsunami[
            'housesDestroyedAmountOrder'] if 'housesDestroyedAmountOrder' in tsunami.keys() else 0
        housesDestroyedAmountOrderTotal = tsunami[
            'housesDestroyedAmountOrderTotal'] if 'housesDestroyedAmountOrderTotal' in tsunami.keys() else 0
        housesDestroyedTotal = tsunami['housesDestroyedTotal'] if 'housesDestroyedTotal' in tsunami.keys() else 0
        injuries = tsunami['injuries'] if 'injuries' in tsunami.keys() else 0
        injuriesAmountOrder = tsunami['injuriesAmountOrder'] if 'injuriesAmountOrder' in tsunami.keys() else 0
        injuriesAmountOrderTotal = tsunami[
            'injuriesAmountOrderTotal'] if 'injuriesAmountOrderTotal' in tsunami.keys() else 0
        injuriesTotal = tsunami['injuriesTotal'] if 'injuriesTotal' in tsunami.keys() else 0
        maxWaterHeight = tsunami['maxWaterHeight'] if 'maxWaterHeight' in tsunami.keys() else 0
        minute = tsunami['minute'] if 'minute' in tsunami.keys() else 0
        missing = tsunami['missing'] if 'missing' in tsunami.keys() else 0
        missingAmountOrder = tsunami['missingAmountOrder'] if 'missingAmountOrder' in tsunami.keys() else 0
        missingAmountOrderTotal = tsunami[
            'missingAmountOrderTotal'] if 'missingAmountOrderTotal' in tsunami.keys() else 0
        missingTotal = tsunami['missingTotal'] if 'missingTotal' in tsunami.keys() else 0
        volcanoEventId = tsunami['volcanoEventId'] if 'volcanoEventId' in tsunami.keys() else 0
        year = tsunami['year'] if 'year' in tsunami.keys() else 0
        warningStatusId = tsunami['warningStatusId'] if 'warningStatusId' in tsunami.keys() else 0
        publish = tsunami['publish'] if 'publish' in tsunami.keys() else False
        month = tsunami['month'] if 'month' in tsunami.keys() else 0
        numDeposits = tsunami['numDeposits'] if 'numDeposits' in tsunami.keys() else 0
        numRunups = tsunami['numRunups'] if 'numRunups' in tsunami.keys() else 0
        regionCode = tsunami['regionCode'] if 'regionCode' in tsunami.keys() else 0
        second = tsunami['second'] if 'second' in tsunami.keys() else 0
        tsIntensity = tsunami['tsIntensity'] if 'tsIntensity' in tsunami.keys() else 0
        tsMtAbe = tsunami['tsMtAbe'] if 'tsMtAbe' in tsunami.keys() else 0
        eqDepth = tsunami['eqDepth'] if 'eqDepth' in tsunami.keys() else 0
        eqMagnitude = tsunami['eqMagnitude'] if 'eqMagnitude' in tsunami.keys() else 0
        tsMtIi = tsunami['tsMtIi'] if 'tsMtIi' in tsunami.keys() else 0
        latitude = tsunami['latitude'] if 'latitude' in tsunami.keys() else 0.0
        longitude = tsunami['longitude'] if 'longitude' in tsunami.keys() else 0.0
        station_to_insert = (
            noaa_id, area, assocDeposits, country, locationName, causeCode, damageAmountOrder, damageAmountOrderTotal, damageMillionsDollars,
            damageMillionsDollarsTotal, day, deaths, deathsAmountOrder, deathsAmountOrderTotal, deathsTotal, earthquakeEventId,
            eventValidity, hour, housesDamaged, housesDamagedAmountOrder, housesDamagedAmountOrderTotal, housesDamagedTotal,
            housesDestroyed, housesDestroyedAmountOrder, housesDestroyedAmountOrderTotal, housesDestroyedTotal, injuries, injuriesAmountOrder, injuriesAmountOrderTotal,
            injuriesTotal, maxWaterHeight, minute, missing, missingAmountOrder, missingAmountOrderTotal, missingTotal,
            month, numDeposits, numRunups, regionCode, second, tsIntensity, tsMtAbe, volcanoEventId, year, warningStatusId,
            publish, eqDepth, eqMagnitude, tsMtIi, latitude, longitude)
        insert_list.append(station_to_insert)
    cur.executemany("INSERT INTO tsunamis_events(noaa_id, area, assocDeposits, country, locationName, causeCode, damageAmountOrder, damageAmountOrderTotal, damageMillionsDollars, \
            damageMillionsDollarsTotal, day, deaths, deathsAmountOrder, deathsAmountOrderTotal, deathsTotal, earthquakeEventId,\
            eventValidity, hour, housesDamaged, housesDamagedAmountOrder, housesDamagedAmountOrderTotal, housesDamagedTotal,\
            housesDestroyed, housesDestroyedAmountOrder, housesDestroyedAmountOrderTotal, housesDestroyedTotal, injuries, injuriesAmountOrder, injuriesAmountOrderTotal,\
            injuriesTotal, maxWaterHeight, minute, missing, missingAmountOrder, missingAmountOrderTotal, missingTotal,\
            month, numDeposits, numRunups, regionCode, second, tsIntensity, tsMtAbe, volcanoEventId, year, warningStatusId,\
            publish, eqDepth, eqMagnitude, tsMtIi, latitude, longitude) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", insert_list)



except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')

conn.commit()
cur.close()

conn.close()
