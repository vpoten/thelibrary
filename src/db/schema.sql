DROP TABLE IF EXISTS Car;
DROP TABLE IF EXISTS JourneyGroup;

CREATE TABLE Car
(
    id        INTEGER   NOT NULL,
    seats     INTEGER   NOT NULL,
    created   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    available INTEGER   NOT NULL
);

CREATE TABLE JourneyGroup
(
    id         INTEGER   NOT NULL,
    people     INTEGER   NOT NULL,
    created    TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    registered TIMESTAMP,
    dropOff    TIMESTAMP,
    carId      INTEGER,
    FOREIGN KEY (carId) REFERENCES Car (id)
);

CREATE UNIQUE INDEX car_id_index on Car (id);
CREATE UNIQUE INDEX journey_id_index on JourneyGroup (id);
CREATE INDEX journey_people_index on JourneyGroup (people);
