--1. Найти все фильмы, продолжительность которых больше средней продолжительности всех фильмов в базе.
SELECT film_id, title, length, (SELECT AVG(length) FROM film) AS avg_ln
FROM film 
WHERE length > (SELECT AVG(length) FROM film)
ORDER BY length 

WITH avg_length AS (SELECT AVG(length) AS avg_len FROM film)

SELECT film_id, title, length, avg_length.avg_len
FROM film, avg_length
WHERE length > avg_length.avg_len
ORDER BY length


--2. Найти сотрудников (staff), которые работают в том же магазине, что и клиент с фамилией SMITH.
SELECT st.staff_id, st.first_name , st.last_name 
FROM customer c
JOIN staff st ON c.store_id = st.store_id
WHERE upper(c.last_name) = 'SMITH'

SELECT st.staff_id, st.first_name , st.last_name 
FROM staff st
WHERE st.store_id = (SELECT c.store_id FROM customer c WHERE upper(c.last_name) = 'SMITH')


--3. Найти клиентов, которые заплатили больше, чем средняя сумма платежа по всей базе.
SELECT c.customer_id, c.first_name, c.last_name,  p.amount , (SELECT AVG(amount) FROM payment) AS avg_pay
FROM customer c
JOIN payment p ON c.customer_id = p.customer_id 
WHERE p.amount > (SELECT AVG(amount) FROM payment)

WITH ap AS (SELECT AVG(amount) AS avg_p FROM payment)

SELECT c.customer_id, c.first_name, c.last_name,  p.amount, ap.avg_p
FROM ap, customer c
JOIN payment p ON c.customer_id = p.customer_id 
WHERE p.amount > ap.avg_p








