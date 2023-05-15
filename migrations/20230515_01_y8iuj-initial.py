from yoyo import step

__depends__ = {}

steps = [
    step("CREATE TABLE stations (id SERIAL PRIMARY KEY, " +
    "station_id VARCHAR(64), name VARCHAR(64), country VARCHAR(64), state VARCHAR(64), latitude DOUBLE PRECISION, longitude DOUBLE PRECISION, " +
            "source VARCHAR(64), modified TIMESTAMP(0))"),
    step("CREATE TABLE station_values (id SERIAL PRIMARY KEY, " +
            "station_id INTEGER, time VARCHAR(64), value VARCHAR(64), datum VARCHAR(64), CONSTRAINT fk_station FOREIGN KEY(station_id) REFERENCES stations(id))")
]
