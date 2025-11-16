--Создайте таблицу с 500 000–1 000 000 строк (например, заказы клиентов). 
--Выполните поиск и сортировку данных без индексов, затем добавьте индекс по ключевому полю (например, status или order_date). 
--Сравните время выполнения запросов до и после добавления индекса и сделайте вывод о влиянии индексации на производительность.

CREATE TABLE IF NOT EXISTS orders_demo (
    order_id      BIGSERIAL,  
    customer_id   INT NOT NULL,
    status        TEXT NOT NULL,
    order_date    DATE NOT NULL,
    amount        NUMERIC(10,2) NOT NULL,
    email         TEXT  
) PARTITION BY RANGE (order_date);

INSERT INTO orders_demo (customer_id, status, order_date, amount, email)
SELECT
    (random()*100000)::INT,                                       
    (ARRAY['New','Processing','Completed','Cancelled'])[
        1 + (floor(random()*4))::INT
    ],
    DATE '2024-01-01' + (random()*365)::INT,                     
    round((random()*500)::numeric, 2),
    'user_' || (100000 + (random()*900000)::INT)::TEXT || '@mail.com'
FROM generate_series(1, 1000000);

DROP INDEX idx_customer_id
DROP INDEX idx_status

CREATE INDEX idx_status ON orders_demo(status)
WHERE status = 'New'

CREATE INDEX idx_order_date ON orders_demo(order_date)


EXPLAIN ANALYZE
SELECT *
FROM orders_demo
WHERE status = 'New' -- Execution Time: 265.595 ms без индекса, Execution Time: 86.885 ms с индексом

EXPLAIN ANALYZE
SELECT *
FROM orders_demo
WHERE order_date BETWEEN '2024-01-20' AND '2024-05-23'  --Execution Time: 222.952 ms без индекса, Execution Time: 120.781 ms с индексом

--Для базы данных с таблицами Пользователи, Продукты и Заказы предложите оптимальные типы индексов под задачи: поиск заказов 
--конкретного пользователя, определение самых популярных продуктов, анализ динамики продаж по месяцам. 
--Обоснуйте выбор индексов (B-Tree, BRIN, GIN) и продемонстрируйте их работу на тестовых данных.

CREATE TABLE IF NOT EXISTS t_customers (
    customer_id      BIGSERIAL PRIMARY KEY,  
    full_name        VARCHAR NOT NULL,
    email         TEXT  
)

INSERT INTO t_customers (full_name, email)
SELECT
    'Name_' || (100000 + (random()*900000)::INT)::TEXT || 'Lastname',                                       
   
    'user_' || (100000 + (random()*900000)::INT)::TEXT || '@mail.com'
FROM generate_series(1, 1000000);

CREATE TABLE IF NOT EXISTS t_products (
    product_id      BIGSERIAL PRIMARY KEY,  
    name        VARCHAR NOT NULL,
    quantity     INT NULL,
    price  NUMERIC(10,2)
)   --В ОДНОМ ЗАКАЗЕ ОДИН ПРОДУКТ

INSERT INTO t_products (name, quantity, price)
SELECT                                    
    'product_' || (100000 + (random()*900000)::INT)::TEXT || 'name',
    (random()*1000)::INT,                     
     round((random()*500)::numeric, 2)
FROM generate_series(1, 1000000);

CREATE TABLE IF NOT EXISTS t_orders (
    order_id      BIGSERIAL PRIMARY KEY,  
    product_id INT NOT NULL,
    customer_id   INT NOT NULL,
    status        TEXT NOT NULL,
    order_date    DATE NOT NULL,
    amount        NUMERIC(10,2) NOT NULL, 
    CONSTRAINT fk_orders_customer
        FOREIGN KEY (customer_id)
        REFERENCES t_customers(customer_id)
        ON DELETE CASCADE,

    CONSTRAINT fk_orders_product
        FOREIGN KEY (product_id)
        REFERENCES t_products(product_id))

INSERT INTO t_orders (product_id, customer_id, status, order_date, amount)
SELECT
    (1+random()*999999)::INT, 
    (1+random()*999999)::INT,
    (ARRAY['New','Processing','Completed','Cancelled'])[
        1 + (floor(random()*4))::INT
    ],
    DATE '2024-01-01' + (random()*365)::INT,                     
    round((random()*500)::numeric, 2)
FROM generate_series(1, 1000000);


-- поиск заказов конкретного пользователя, определение самых популярных продуктов, анализ динамики продаж по месяцам

CREATE INDEX idx_customer_id ON t_orders(customer_id)

EXPLAIN ANALYZE
SELECT *
FROM t_orders
WHERE customer_id = 851455 -- Execution Time: 332.767 ms без индекса, Execution Time: 0.181 ms с индексом

EXPLAIN ANALYZE
SELECT product_id, SUM(amount) AS total_am
FROM t_orders 
GROUP BY product_id
ORDER BY total_am DESC -- индекс не эффективен 

EXPLAIN ANALYZE
SELECT COUNT(order_id) AS ord_cnt, 
EXTRACT(MONTH FROM order_date) AS mon
FROM t_orders
GROUP BY mon
ORDER BY ord_cnt DESC  --Execution Time: 645.178 ms без индекса, -- Execution Time: 548.668 ms индекс не применился

CREATE INDEX idx_t_orders_month ON t_orders (EXTRACT(MONTH FROM order_date));

