from yoyo import step

__depends__ = {}

steps = [
    step('CREATE EXTENSION IF NOT EXISTS "uuid-ossp"'),
    step("CREATE TABLE stations (id uuid DEFAULT uuid_generate_v4 () PRIMARY KEY, " +
    "station_id VARCHAR(64), name VARCHAR(64), country VARCHAR(64), state VARCHAR(64), latitude DOUBLE PRECISION, longitude DOUBLE PRECISION, source VARCHAR(64))"),
    step("CREATE TABLE station_values (id uuid DEFAULT uuid_generate_v4 () PRIMARY KEY, " +
            "station_id uuid, time TIMESTAMP(0), value VARCHAR(64), datum VARCHAR(64), CONSTRAINT fk_station FOREIGN KEY(station_id) REFERENCES stations(id))"),
    step("CREATE TABLE tsunamis_events (id uuid DEFAULT uuid_generate_v4 () PRIMARY KEY, " +
            "noaa_id INTEGER, area VARCHAR(64), assocDeposits VARCHAR(64), country VARCHAR(64), locationName VARCHAR(64), causeCode INTEGER, damageAmountOrder INTEGER, damageAmountOrderTotal INTEGER, damageMillionsDollars INTEGER, damageMillionsDollarsTotal INTEGER, " +
            "day INTEGER, deaths INTEGER, deathsAmountOrder INTEGER, deathsAmountOrderTotal INTEGER, deathsTotal INTEGER, earthquakeEventId INTEGER, " +
            "eventValidity INTEGER, hour INTEGER, housesDamaged INTEGER, housesDamagedAmountOrder INTEGER, housesDamagedAmountOrderTotal INTEGER, housesDamagedTotal INTEGER, " +
            "housesDestroyed INTEGER, housesDestroyedAmountOrder INTEGER, housesDestroyedAmountOrderTotal INTEGER, housesDestroyedTotal INTEGER, injuries INTEGER, injuriesAmountOrder INTEGER, injuriesAmountOrderTotal INTEGER, " +
            "injuriesTotal INTEGER, maxWaterHeight INTEGER, minute INTEGER, missing INTEGER, missingAmountOrder INTEGER, missingAmountOrderTotal INTEGER, missingTotal INTEGER, " +
            "month INTEGER, numDeposits INTEGER, numRunups INTEGER, regionCode INTEGER, second INTEGER, tsIntensity INTEGER, tsMtAbe INTEGER, " +
            "volcanoEventId INTEGER, year INTEGER, warningStatusId INTEGER, publish BOOL, eqDepth INTEGER, eqMagnitude INTEGER, tsMtIi INTEGER, " +
            "latitude DOUBLE PRECISION, longitude DOUBLE PRECISION)")
]
