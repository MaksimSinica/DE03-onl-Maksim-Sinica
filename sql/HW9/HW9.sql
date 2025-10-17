--1. Операции обновления с проверкой условий
--Создайте транзакцию для таблицы accounts, которая уменьшает баланс на 1000 для
--всех счетов, чей баланс превышает 5000. Если операция прошла успешно,
--зафиксируйте изменения. В случае ошибки откатите транзакцию.
CREATE TABLE accounts 
	(acc_id SERIAL PRIMARY KEY, 
	number INT NOT NULL,
	balance DECIMAL(10,2),
	date TIMESTAMP)
	
INSERT INTO accounts(number, balance, date)
VALUES (123, 3000.42, now()),
(345, 1000.42, (now()+ '1 days'::INTERVAL)),
(356, 6000.23, (now()+ '2 days'::INTERVAL)),
(134, 62300.42, (now()+ '3 days'::INTERVAL)),
(1225, 4000.54, (now()+ '4 days'::INTERVAL)),
(2142, 24000.42, (now()+ '5 days'::INTERVAL)),
(1322, 2000.22, (now()+ '6 days'::INTERVAL));

BEGIN;
UPDATE accounts
SET balance = balance - 1000
WHERE balance > 5000;
COMMIT;

--2. Последовательные вставки с проверкой ошибок
--Напишите транзакцию для таблицы inventory, которая добавляет новый товар и
--сразу же обновляет количество на складе. Если хотя бы одна из операций завершится с
--ошибкой, отмените транзакцию.
BEGIN;
INSERT INTO inventory (film_id, store_id, last_update)
VALUES (453, 1, now());
-- Здесь нет как такового склада. Нет отдельной таблицы или колонки  под количество. Количество регулируется добавлением строк.
INSERT INTO inventory (film_id, store_id, last_update)
VALUES (450, 2, now());

INSERT INTO inventory (film_id, store_id, last_update)
VALUES (465, 2, now());
COMMIT;
--3. Создание резервной копии и удаление данных
--Создайте транзакцию, которая сначала создает резервную копию таблицы users в
--users_backup, а затем удаляет все записи из users, чей статус равен 'inactive'.
--Если операция удаления не удалась, откатите транзакцию.
CREATE TABLE users 
(user_id SERIAL PRIMARY KEY, 
full_name VARCHAR(30) NOT NULL, 
email VARCHAR(20) UNIQUE,
start_date TIMESTAMP,
status VARCHAR(10))

INSERT INTO users(full_name, email, start_date, status)
VALUES ('Максим Синица', 'maks@mail.ru', now(), 'active'),
		('Кларк Кент', 'klark@mail.ru', now(), 'inactive'),
		('Джон Дефо', 'defoe@mail.ru', now(), 'inactive'),
		('Макс Ферстаппен', 'maksf@mail.ru', now(), 'active');
BEGIN;
CREATE TABLE users_backup AS TABLE users

DELETE FROM users
WHERE status = 'inactive'
COMMIT;





