--1. Создать базу данных library, внутри неё таблицу books с полями: book_id (целое число, первичный ключ, автоинкремент), 
--title (строка до 200 символов, не пустая), author (строка до 100 символов), published_year (целое число, год издания). 
--После этого добавить в таблицу три книги.
CREATE DATABASE library;

CREATE TABLE IF NOT EXISTS books (
	book_id serial PRIMARY KEY,
	title varchar(200) NOT NULL,
	author varchar(100),
	published_year INT);

INSERT INTO books (title, author, published_year)
VALUES ('Мастер и Маргарита', 'Булгаков', '1966'),
('Евгений Онегин', 'Пушкин', '1823'),
('Война и Мир', 'Толстой', '1865');

--2.В таблице books нужно изменить структуру: добавить новый столбец genre типа VARCHAR(50),
--переименовать столбец title в book_title, а затем удалить столбец published_year.
ALTER TABLE books ADD COLUMN genre VARCHAR(50);
ALTER TABLE books RENAME COLUMN title TO book_title;
ALTER TABLE books DROP COLUMN published_year;

--3. В таблице books удалить все записи, где автор равен 'Unknown'. 
--Создать таблицу archived_books с теми же полями, что и у books, перенести в неё все книги автора 'J.K. Rowling',
--после чего полностью удалить таблицу archived_books.
DELETE FROM books 
WHERE author = 'Unknow';

CREATE TABLE IF NOT EXISTS archived_books (
	book_id serial PRIMARY KEY,
	book_title VARCHAR(200) NOT NULL,
	author VARCHAR(100),
	genre VARCHAR(50));

INSERT INTO archived_books (book_id, book_title, author, genre)
SELECT *
FROM books 
WHERE author = 'J.K. Rowling';

DROP TABLE archived_books;

