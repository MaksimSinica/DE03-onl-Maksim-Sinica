--1. Выведите сводку по семейным фильмам (жанр Family), выпущенным начиная с 2007 года. 
--Для каждого года выпуска определите количество фильмов, среднюю, минимальную и максимальную продолжительность. 
--Результат отсортируйте по году выпуска в порядке убывания.
SELECT f. release_year, COUNT(f.film_id) AS cnt_film, AVG(f.length) AS avg_length, MIN(f.length) AS min_length, MAX(f.length) AS max_length
FROM film f
JOIN film_category fc ON (f.film_id = fc.film_id)
JOIN category c ON (fc.category_id = c.category_id)
WHERE c.name = 'Family' AND f.release_year >= 2007
GROUP BY f.release_year
ORDER BY f.release_year desc

--2. Определите суммарную выручку и количество транзакций за 2007 год по каждой стране проживания клиентов. 
--Отсортируйте результат по выручке в порядке убывания и выведите только первые 10 стран.
SELECT cn.country, SUM(p.amount) AS sum_amount, COUNT(p.payment_id) AS cnt_payment
FROM customer c 
JOIN address a ON (c.address_id = a.address_id)
JOIN city ct ON (a.city_id = ct.city_id)
JOIN country cn ON (ct.country_id = cn.country_id)
JOIN payment p ON (c.customer_id = p.customer_id)
WHERE EXTRACT(YEAR FROM p.payment_date) = 2017 --2007 года нет в БД
GROUP BY cn.country
ORDER BY sum_amount DESC
LIMIT 10

--3. Найдите пять категорий фильмов с наибольшим количеством фильмов. 
--Для каждой категории выведите количество фильмов и среднюю стоимость аренды. 
--Результат отсортируйте по числу фильмов в порядке убывания, а при равенстве — по названию категории.

SELECT c.name, COUNT(f.film_id) AS cnt_film, ROUND(AVG(f.rental_rate), 2) AS avg_rental_rate
FROM film f
JOIN film_category fc ON (f.film_id = fc.film_id)
JOIN category c ON (fc.category_id = c.category_id)
GROUP BY c.name
ORDER BY cnt_film DESC, c.name
LIMIT 5





