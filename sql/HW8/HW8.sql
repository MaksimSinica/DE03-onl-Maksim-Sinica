--1. Составные ключи и связи в цепочке таблиц
--Создайте три таблицы:
--departments(dept_id, dept_name) — первичный ключ dept_id.
--employees(emp_id, dept_id, full_name) — первичный ключ emp_id, внешний ключ dept_id ссылается на departments.
--projects(project_id, dept_id, project_name) — первичный ключ project_id, внешний ключ dept_id ссылается на departments.
--Теперь создайте таблицу employee_projects, где хранится назначение сотрудников на проекты.
--В ней должен быть составной первичный ключ (emp_id, project_id) и два внешних ключа, ссылающихся на employees(emp_id) и projects(project_id).
--Вставьте корректные данные и попробуйте вставить запись с несуществующим emp_id или project_id.
CREATE TABLE  IF NOT EXISTS departaments 
	(dept_id SERIAL PRIMARY KEY,
	dept_name VARCHAR(20) NOT NULL);
	
CREATE TABLE  IF NOT EXISTS employees 
	(emp_id SERIAL PRIMARY KEY,
	full_name VARCHAR(20) NOT NULL,
	dept_id INT NOT NULL,
	FOREIGN KEY (dept_id) REFERENCES departaments(dept_id));

CREATE TABLE  IF NOT EXISTS projects 
	(project_id SERIAL PRIMARY KEY,
	 dept_id INT,
	 project_name VARCHAR(40) NOT NULL,
	 FOREIGN KEY (dept_id) REFERENCES departaments(dept_id));
	
CREATE TABLE  IF NOT EXISTS employee_projects 
	(emp_id INT NOT NULL,
	project_id INT NOT NULL,
	PRIMARY KEY (emp_id, project_id),
	FOREIGN KEY (emp_id) REFERENCES employees(emp_id),
	FOREIGN KEY (project_id) REFERENCES projects(project_id));



INSERT INTO departaments(dept_name)
VALUES 
	('marketing'),
	('economic'),
	('techno');

INSERT INTO employees(full_name, dept_id)
VALUES 
	('Maksim Sinica', (SELECT dept_id FROM departaments WHERE lower(dept_name) = 'techno')),
	('Mark Echo', (SELECT dept_id FROM departaments WHERE lower(dept_name) = 'economic')),
	('Inna Dou', (SELECT dept_id FROM departaments WHERE lower(dept_name) = 'marketing'));

INSERT INTO projects(dept_id, project_name)
VALUES 
	((SELECT dept_id FROM departaments WHERE lower(dept_name) = 'techno'), 'electrical diagram'),
	((SELECT dept_id FROM departaments WHERE lower(dept_name) = 'economic'), 'reports'),
	((SELECT dept_id FROM departaments WHERE lower(dept_name) = 'marketing'), 'sales');

INSERT INTO employee_projects (emp_id, project_id)
VALUES
	((SELECT emp_id FROM employees WHERE full_name = 'Maksim Sinica'), (SELECT project_id FROM projects WHERE project_name = 'electrical diagram')),
	((SELECT emp_id FROM employees WHERE full_name = 'Mark Echo'), (SELECT project_id FROM projects WHERE project_name = 'reports')),
	((SELECT emp_id FROM employees WHERE full_name = 'Inna Dou'), (SELECT project_id FROM projects WHERE project_name = 'sales'));

INSERT INTO employee_projects (emp_id, project_id)
VALUES
	((SELECT emp_id FROM employees WHERE full_name = 'Maksim Sinica'), 4);
--2. Каскадное удаление и ограничение ссылочной целостности
--В таблицах из задачи 1 добавьте правило: при удалении отдела (departments) должны автоматически удаляться все его сотрудники и проекты, 
--но записи в employee_projects при этом не должны удаляться автоматически — база должна выдавать ошибку при попытке удаления.
--Проверьте поведение каскадов (ON DELETE CASCADE, ON DELETE RESTRICT).
DROP TABLE employee_projects;
DROP TABLE employees;
DROP TABLE projects;
DROP TABLE departaments;

CREATE TABLE  IF NOT EXISTS departaments 
	(dept_id SERIAL PRIMARY KEY,
	dept_name VARCHAR(20) NOT NULL);
	
CREATE TABLE  IF NOT EXISTS employees 
	(emp_id SERIAL PRIMARY KEY,
	full_name VARCHAR(20) NOT NULL,
	dept_id INT NOT NULL,
	FOREIGN KEY (dept_id) REFERENCES departaments(dept_id) ON DELETE CASCADE);

CREATE TABLE  IF NOT EXISTS projects 
	(project_id SERIAL PRIMARY KEY,
	 dept_id INT,
	 project_name VARCHAR(40) NOT NULL,
	 FOREIGN KEY (dept_id) REFERENCES departaments(dept_id) ON DELETE CASCADE);
	
CREATE TABLE  IF NOT EXISTS employee_projects 
	(emp_id INT NOT NULL,
	project_id INT NOT NULL,
	PRIMARY KEY (emp_id, project_id),
	FOREIGN KEY (emp_id) REFERENCES employees(emp_id),
	FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE RESTRICT);

INSERT INTO departaments(dept_name)
VALUES 
	('marketing'),
	('economic'),
	('techno');

INSERT INTO employees(full_name, dept_id)
VALUES 
	('Maksim Sinica', (SELECT dept_id FROM departaments WHERE lower(dept_name) = 'techno')),
	('Mark Echo', (SELECT dept_id FROM departaments WHERE lower(dept_name) = 'economic')),
	('Inna Dou', (SELECT dept_id FROM departaments WHERE lower(dept_name) = 'marketing'));

INSERT INTO projects(dept_id, project_name)
VALUES 
	((SELECT dept_id FROM departaments WHERE lower(dept_name) = 'techno'), 'electrical diagram'),
	((SELECT dept_id FROM departaments WHERE lower(dept_name) = 'economic'), 'reports'),
	((SELECT dept_id FROM departaments WHERE lower(dept_name) = 'marketing'), 'sales');

INSERT INTO employee_projects (emp_id, project_id)
VALUES
	((SELECT emp_id FROM employees WHERE full_name = 'Maksim Sinica'), (SELECT project_id FROM projects WHERE project_name = 'electrical diagram')),
	((SELECT emp_id FROM employees WHERE full_name = 'Mark Echo'), (SELECT project_id FROM projects WHERE project_name = 'reports')),
	((SELECT emp_id FROM employees WHERE full_name = 'Inna Dou'), (SELECT project_id FROM projects WHERE project_name = 'sales'));

DELETE FROM departaments
WHERE dept_name = 'marketing'
--3.Оптимизация поиска с индексами
--Для таблицы employees создайте три индекса:
--• по dept_id;
--• по full_name;
--• составной по (dept_id, full_name).
--С помощью EXPLAIN ANALYZE сравните выполнение запросов:
--SELECT * FROM employees WHERE dept_id = 10;
--SELECT * FROM employees WHERE full_name = 'Ivan Ivanov';
--SELECT * FROM employees WHERE dept_id = 10 AND full_name = 'Ivan Ivanov';
--Объясните, в каких случаях используется один индекс, составной индекс или оба сразу.
CREATE INDEX idx_dept_id ON employees(dept_id)
CREATE INDEX idx_full_name ON employees(full_name)
CREATE INDEX idx_dept_id_full_name ON employees(dept_id, full_name)

INSERT INTO departaments (dept_name)
SELECT
   'marketing' || i
FROM generate_series(1, 1000000) AS s(i);

INSERT INTO employees (full_name, dept_id)
SELECT
    CASE WHEN i % 5 = 0 THEN 'Ivan Ivanov' ELSE 'Oth Other' || i END, (i+3)
FROM generate_series(1, 1000000) AS s(i);

EXPLAIN ANALYZE	
SELECT * FROM employees WHERE dept_id = 10 --Index Scan using idx_dept_id_full_name
EXPLAIN ANALYZE
SELECT * FROM employees WHERE full_name = 'Ivan Ivanov' --Seq Scan (непонятно почему здесь не применился индекс по фуллнэйму в 1000000 строк фамилии только на I и на O)
EXPLAIN ANALYZE
SELECT * FROM employees WHERE dept_id = 10 AND full_name = 'Ivan Ivanov' --Index Scan using idx_dept_id_full_name

--4. Избыточное индексирование и производительность
--Добавьте в таблицу employees ещё один индекс по full_name и сравните результаты вставки 100 000 строк с и без него.
--Используйте EXPLAIN ANALYZE INSERT INTO ... SELECT ... для оценки.
--Объясните, почему большое количество индексов замедляет операции вставки и обновления, и в каких случаях это оправдано.
EXPLAIN ANALYZE -- Execution Time: 5147.115 ms
INSERT INTO employees (full_name, dept_id)
SELECT
    CASE WHEN i % 5 = 0 THEN 'Ivan Ivanov' ELSE 'Oth Other' || i END, (i+3)
FROM generate_series(1000001, 1100000) AS s(i);

CREATE INDEX idx_full_name_2 ON employees(full_name)

EXPLAIN ANALYZE --Execution Time: 6601.102 ms
INSERT INTO employees (full_name, dept_id)
SELECT
    CASE WHEN i % 5 = 0 THEN 'Ivan Ivanov' ELSE 'Oth Other' || i END, (i+3)
FROM generate_series(1100001, 1200000) AS s(i);

--Время вставки увеличилось из-за необходимости обновления еще одного созданного индекса. 
--Большое количество индексов оправдано только в тех случаях если очень большая таблица и 
--в выборке применяются всегда разные поля для фильтрации или группировки.


--5. Реальный сценарий выбора оптимального индекса
--В таблице projects добавьте поля start_date и budget.
--Проанализируйте три типа запросов:
--1. фильтр по start_date (диапазон за год),
--2. фильтр по budget > 1000000,
--3. фильтр одновременно по дате и бюджету.
--Создайте подходящие индексы (B-tree или составной) и объясните, какой из них эффективнее для каждого случая и почему.
ALTER TABLE projects ADD COLUMN start_date DATE,
ADD COLUMN budget DECIMAL;

INSERT INTO projects (dept_id, project_name,start_date,budget)
SELECT i, 'Projectr' || i, (now() + (i || ' days')::INTERVAL), (900000 + 30*i)
FROM generate_series(5, 1000) AS s(i);
EXPLAIN ANALYZE
SELECT * FROM projects WHERE start_date BETWEEN '2026-01-01' AND '2027-01-01' --Execution Time: 0.228 ms без индекса

EXPLAIN ANALYZE
SELECT * FROM projects WHERE budget > 911000 --Execution Time: 0.310 ms без индекса

EXPLAIN ANALYZE
SELECT * FROM projects WHERE (start_date BETWEEN '2026-01-01' AND '2027-01-01') AND budget > 911000 --Execution Time: 0.567 ms без индекса
CREATE INDEX idx_start_date ON projects(start_date)
CREATE INDEX idx_budget ON projects(budget)
CREATE INDEX idx_start_date_budget ON projects(start_date, budget)

EXPLAIN ANALYZE
SELECT * FROM projects WHERE start_date BETWEEN '2026-01-01' AND '2027-01-01'--Index Scan using idx_start_date  Execution Time: 0.316 ms(маленькая таблица)

EXPLAIN ANALYZE
SELECT * FROM projects WHERE budget > 911000 --Seq Scan Execution Time: 0.388 ms(низкая селективность)

EXPLAIN ANALYZE
SELECT * FROM projects WHERE (start_date BETWEEN '2026-01-01' AND '2027-01-01') AND budget > 911000 --Index Scan using idx_start_date Execution Time: 0.287 ms(выбран индекс по дате из-за низкой селективности индекса по бюджету)
