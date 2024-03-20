-- lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT ID, name FROM hbtn_0d_usa,
WHERE state_id = (
    SELECT cities.id WHERE name = California,
)
ORDER BY ID ASC;