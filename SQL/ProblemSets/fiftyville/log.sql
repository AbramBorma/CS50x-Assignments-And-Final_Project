-- Keep a log of any SQL queries you execute as you solve the mystery.
/* Information from the tables:

1- From crime_scene_reports:

SELECT * FROM crime_scene_reports WHERE year = 2023 AND month = 7 AND day = 28 AND street = 'Humphrey Street';

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                       description                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery. |
| Littering took place at 16:36. No known witnesses.                                                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

2- From interviews:

SELECT * FROM interviews WHERE year = 2023 AND month = 7 AND day = 28 AND id > 160 AND id < 164;

+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|  name   |                                                                                                                                                     transcript                                                                                                                                                      |
+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Ruth    | Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away. If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.                                                          |
| Eugene  | I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.                                                                                                 |
| Raymond | As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person on the other end of the phone to purchase the flight ticket. |
+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Data from Interviews:

Interview 1:

- The thief left the bakery within 10 minutes of the theft.
- The thief rode a car in the bakery parking lot.

Interview 2:

- The thief withdrew money from an ATM on Legget Street.

Interview 3:

- As the thief was leaving the bakery, they called someone who talked to them for less than a 60 seconds.
- The thief was planning to take the earliest flight out of Fiftyville on 2023-7-29.
- The thief then asked the person on the other end of the phone to purchase the flight ticket.

Following the data from Interviews:*/

-- Getting the thief's name:

SELECT *
FROM people
WHERE passport_number IN
(
    SELECT passport_number
    FROM passengers
    JOIN flights ON passengers.flight_id = flights.id
    JOIN airports AS origin ON flights.origin_airport_id = origin.id
    JOIN airports AS destination ON flights.destination_airport_id = destination.id
    WHERE passport_number IN
    (
        SELECT passport_number
        FROM people
        JOIN bank_accounts ON people.id = bank_accounts.person_id
        WHERE license_plate IN
        (
            SELECT license_plate
            FROM bakery_security_logs
            WHERE (year, month, day, hour, activity) = (2023, 7, 28, 10, 'exit') AND minute BETWEEN 15 AND 25
        )
        AND phone_number IN
        (
            SELECT caller
            FROM phone_calls
            WHERE (year, month, day) = (2023, 7, 28) AND duration < 60
        )
        AND account_number IN
        (
            SELECT account_number
            FROM atm_transactions
            WHERE (year, month, day, atm_location, transaction_type) = (2023, 7, 28, 'Leggett Street', 'withdraw')
        )
    )
    AND (year, month, day) = (2023, 7, 29) ORDER BY hour LIMIT 1
);

-- Getting the thief's destination city.

SELECT passport_number, destination.city
FROM passengers
JOIN flights ON passengers.flight_id = flights.id
JOIN airports AS origin ON flights.origin_airport_id = origin.id
JOIN airports AS destination ON flights.destination_airport_id = destination.id
WHERE passport_number = 5773159633;

-- Finding out thief's accomplice.

SELECT *
FROM people
WHERE phone_number IN
(
    SELECT receiver
    FROM phone_calls
    WHERE caller = '(367) 555-5533'
    AND (year, month, day) = (2023, 7, 28) AND duration < 60
);

/* This is another longer solution:

code:

CREATE TABLE thief_name (
    id INTEGER,
    thief_name TEXT,
    PRIMARY KEY (id)
);

CREATE TABLE thief_destination (
    id INTEGER,
    destination TEXT,
    PRIMARY KEY (id),
    FOREIGN KEY (id) REFERENCES thief_name(id)
);

CREATE TABLE thief_accomplice (
    id INTEGER,
    thief_accomplice TEXT,
    PRIMARY KEY (id),
    FOREIGN KEY (id) REFERENCES thief_name(id));



INSERT INTO thief_name (thief_name)
SELECT name
FROM people
WHERE passport_number IN
(
    SELECT passport_number
    FROM passengers
    JOIN flights ON passengers.flight_id = flights.id
    JOIN airports AS origin ON flights.origin_airport_id = origin.id
    JOIN airports AS destination ON flights.destination_airport_id = destination.id
    WHERE passport_number IN
    (
        SELECT passport_number
        FROM people
        JOIN bank_accounts ON people.id = bank_accounts.person_id
        WHERE license_plate IN
        (
            SELECT license_plate
            FROM bakery_security_logs
            WHERE (year, month, day, hour, activity) = (2023, 7, 28, 10, 'exit') AND minute BETWEEN 15 AND 25
        )
        AND phone_number IN
        (
            SELECT caller
            FROM phone_calls
            WHERE (year, month, day) = (2023, 7, 28) AND duration < 60
        )
        AND account_number IN
        (
            SELECT account_number
            FROM atm_transactions
            WHERE (year, month, day, atm_location, transaction_type) = (2023, 7, 28, 'Leggett Street', 'withdraw')
        )
    )
    AND (year, month, day) = (2023, 7, 29) ORDER BY hour LIMIT 1
);
INSERT INTO thief_destination(destination)
SELECT destination.city
FROM passengers
JOIN flights ON passengers.flight_id = flights.id
JOIN airports AS origin ON flights.origin_airport_id = origin.id
JOIN airports AS destination ON flights.destination_airport_id = destination.id
WHERE passport_number IN
(
    SELECT passport_number
    FROM people
    JOIN bank_accounts ON people.id = bank_accounts.person_id
    WHERE license_plate IN
    (
        SELECT license_plate
        FROM bakery_security_logs
        WHERE (year, month, day, hour, activity) = (2023, 7, 28, 10, 'exit') AND minute BETWEEN 15 AND 25
    )
    AND phone_number IN
    (
        SELECT caller
        FROM phone_calls
        WHERE (year, month, day) = (2023, 7, 28) AND duration < 60
    )
    AND account_number IN
    (
        SELECT account_number
        FROM atm_transactions
        WHERE (year, month, day, atm_location, transaction_type) = (2023, 7, 28, 'Leggett Street', 'withdraw')
    )
)
AND (year, month, day) = (2023, 7, 29) ORDER BY hour LIMIT 1;

INSERT INTO thief_accomplice(thief_accomplice)
SELECT name
FROM people
WHERE phone_number IN
(
    SELECT receiver
    FROM phone_calls
    WHERE caller IN

    (
        SELECT phone_number
        FROM people
        WHERE passport_number IN
        (
            SELECT passport_number
            FROM passengers
            JOIN flights ON passengers.flight_id = flights.id
            JOIN airports AS origin ON flights.origin_airport_id = origin.id
            JOIN airports AS destination ON flights.destination_airport_id = destination.id
            WHERE passport_number IN
            (
                SELECT passport_number
                FROM people
                JOIN bank_accounts ON people.id = bank_accounts.person_id
                WHERE license_plate IN
                (
                    SELECT license_plate
                    FROM bakery_security_logs
                    WHERE (year, month, day, hour, activity) = (2023, 7, 28, 10, 'exit') AND minute BETWEEN 15 AND 25
                )
                AND phone_number IN
                (
                    SELECT caller
                    FROM phone_calls
                    WHERE (year, month, day) = (2023, 7, 28) AND duration < 60
                )
                AND account_number IN
                (
                    SELECT account_number
                    FROM atm_transactions
                    WHERE (year, month, day, atm_location, transaction_type) = (2023, 7, 28, 'Leggett Street', 'withdraw')
                )
            )
            AND (year, month, day) = (2023, 7, 29) ORDER BY hour LIMIT 1
        )

    )

    AND (year, month, day) = (2023, 7, 28) AND duration < 60
);


SELECT thief_name.id, thief_name, destination, thief_accomplice
FROM thief_name
JOIN thief_destination ON thief_name.id = thief_destination.id
JOIN thief_accomplice ON thief_name.id = thief_accomplice.id */
