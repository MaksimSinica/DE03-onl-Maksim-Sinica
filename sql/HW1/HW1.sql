CREATE TABLE IF NOT EXISTS movies 
	(movie_id serial PRIMARY KEY ,
	title varchar, 
	genre varchar, 
	release_year int, 
	duration int);

CREATE TABLE IF NOT EXISTS tickets 
	(ticket_id serial PRIMARY KEY ,
	movie_id int,
	customer_name varchar, 
	seat_number int, 
	price numeric(8,2),
	FOREIGN KEY (movie_id) REFERENCES movies(movie_id));

INSERT INTO movies (title, genre, release_year, duration)
VALUES 
	('Терминатор', 'Боевик', 1985, 128),
	('Властелин колец', 'Фэнтези', 2005, 186),
	('Рэмбо', 'Боевик', 1982, 114),
	('Мальчишник в Вегасе', 'Комедия', 2009, 132),
	('1+1', 'Драма', 2010, 165);

INSERT INTO tickets (movie_id, customer_name, seat_number, price)
VALUES 
	(1, 'Максим', 5, 14.25),
	(2, 'Дмитрий', 13, 25.84),
	(1, 'Лена', 25, 14.25),
	(3, 'Павел', 2, 10),
	(5, 'Ирина', 9, 17.2);

SELECT *
FROM movies m
WHERE m.genre = 'Боевик'

SELECT *
FROM movies m 
WHERE m.release_year > 2000

SELECT *
FROM tickets t 
WHERE t.price > 15

SELECT *
FROM movies m 
WHERE m.title LIKE '%колец%'







