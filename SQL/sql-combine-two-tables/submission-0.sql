-- Write your query below

SELECT person.first_name, person.last_name, address.city, address.state
from person
LEFT JOIN address ON address.person_id = person.person_id