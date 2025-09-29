--1. Повысить цену аренды всех фильмов категории Comedy на 10 процентов, используя обновление с подзапросом к таблицам film_category и category.
UPDATE film f 
SET rental_rate = f.rental_rate * 1.1
WHERE film_id IN (SELECT film_id FROM film_category fc JOIN category c ON fc.category_id = c.category_id WHERE lower(c."name") = 'comedy')
RETURNING *
--2. Удалить всех клиентов, которые находятся в статусе active = 0 и при этом не имеют ни одной записи в таблице rental.

DELETE FROM customer 
WHERE active = 0 AND customer_id NOT IN (SELECT customer_id FROM rental)
RETURNING *
--3. Добавить новую запись в таблицу rental для любого фильма категории Action, при этом арендатором должен быть клиент с 
--наибольшим количеством аренд в истории, используя вставку с подзапросом.
ALTER TABLE rental ADD COLUMN new_record varchar(10);

WITH t1 AS (SELECT rental_id
		FROM rental r
		JOIN inventory i ON i.inventory_id = r.inventory_id 
		JOIN film f ON f.film_id = i.film_id 
		JOIN film_category fc ON f.film_id = fc.film_id 
		JOIN category c ON fc.category_id = c.category_id
		WHERE lower(c.name) = 'action' AND r.customer_id = (SELECT customer_id FROM rental GROUP BY customer_id ORDER BY COUNT(rental_id) DESC LIMIT 1));

UPDATE rental
SET new_record = 'RICH CUST'
WHERE rental_id = (SELECT rental_id FROM t1 LIMIT 1);
RETURNING *

