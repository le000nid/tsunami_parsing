from yoyo import step

__depends__ = {}

steps = [
    step('CREATE EXTENSION IF NOT EXISTS "uuid-ossp"'),
    step("CREATE TABLE stations (id uuid DEFAULT uuid_generate_v4 () PRIMARY KEY, " +
    "station_id VARCHAR(64), name VARCHAR(64), country VARCHAR(64), state VARCHAR(64), latitude DOUBLE PRECISION, longitude DOUBLE PRECISION, source VARCHAR(64))"),
    step("CREATE TABLE station_values (id uuid DEFAULT uuid_generate_v4 () PRIMARY KEY, " +
            "station_id uuid, time TIMESTAMP(0), value VARCHAR(64), datum VARCHAR(64), CONSTRAINT fk_station FOREIGN KEY(station_id) REFERENCES stations(id))")
]
