
--1. Вывести названия фильмов жанра Action, которые сняты на английском языке. 
--Отсортировать по году выпуска (от новых к старым) и вывести первые 20 строк.

SELECT f.title, l.name, c.name, f.release_year
FROM film f
JOIN film_category fc ON (f.film_id = fc.film_id)
JOIN category c ON (c.category_id = fc.category_id)
JOIN "language" l ON (l.language_id = f.language_id)
WHERE c.name = 'Action' AND l.name = 'English'
ORDER BY f.release_year DESC
LIMIT 20

--2. Показать клиентов и города магазинов, к которым они относятся. 
--Вывести только тех клиентов, у которых город начинается на букву A. 
--Отсортировать по фамилии клиента, ограничить результат 25 строками.

SELECT c.first_name, c.last_name, ct.city
FROM customer c 
JOIN store s ON (s.store_id = c.store_id)
JOIN address a ON (a.address_id = s.address_id)
JOIN city ct ON (ct.city_id  = a.city_id)
WHERE ct.city LIKE 'A%'
ORDER BY c.last_name
LIMIT 25

--3. Показать список клиентов, фильмов и сумм платежей, где сумма оплаты больше 5. 
--Отсортировать по сумме (по убыванию), затем по дате платежа (по убыванию). 
--Ограничить результат 30 строками.

SELECT c.first_name , c.last_name, f.title, p.amount 
FROM customer c 
JOIN payment p ON (c.customer_id =p.customer_id)
JOIN rental r ON (r.rental_id = p.rental_id)
JOIN inventory i ON (i.inventory_id  = r.inventory_id)
JOIN film f ON (f.film_id = i.film_id)
WHERE p.amount > 5
ORDER BY p.amount DESC, p.payment_date DESC 
LIMIT 30

--4. Вывести все фильмы, в которых снимался актёр или актриса с фамилией MONROE. 
--Отсортировать по названию фильма.

SELECT f.title
FROM film f
JOIN film_actor fa  ON (fa.film_id = f.film_id)
JOIN actor a ON (a.actor_id = fa.actor_id)
WHERE a.last_name = 'MONROE'
ORDER BY f.title

--5. Показать список клиентов и фильмов, которые они арендовали и ещё не вернули (return_date IS NULL). 
--Отсортировать по дате аренды (от новых к старым) и вывести 20 строк.

SELECT c.customer_id , c.first_name , c.last_name , f.film_id, f.title 
FROM customer c 
JOIN rental r ON (c.customer_id = r.customer_id)
JOIN inventory i ON (i.inventory_id = r.inventory_id)
JOIN film f ON (f.film_id = i.film_id)
WHERE r.return_date IS NULL
ORDER BY r.rental_date DESC 
LIMIT 20



