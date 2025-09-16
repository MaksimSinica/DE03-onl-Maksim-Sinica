/*1. Выведите 15 актёров из таблицы actor, у которых фамилия начинается с буквы M, а дата последнего обновления 
(last_update) попадает в 2017 год. Отсортируйте результат по фамилии (возр.), затем по имени (возр.).*/

SELECT *
FROM actor a 
WHERE a.last_name LIKE 'M%' AND a.last_update BETWEEN '2017-01-01' AND '2018-01-01'
ORDER BY a.last_name, a.first_name 

/*2. Выведите сотрудников из таблицы staff, у которых active = 1 и адрес электронной почты оканчивается на .com. 
Отсортируйте по фамилии (возр.), затем по имени (возр.). Покажите только первые 10 строк*/.

SELECT *
FROM staff s 
WHERE s.active = True AND s.email LIKE '%.com'
ORDER BY s.last_name, s.first_name 
LIMIT 10

/*3. Выведите список платежей, у которых сумма находится в диапазоне от 8.00 до 10.00 включительно. 
Отсортируйте их по дате платежа (возрастание), а при совпадении даты — по сумме (убывание). 
Покажите только первые 40 записей.*/

SELECT *
FROM payment p
WHERE p.amount BETWEEN 8 AND 10
ORDER BY p.payment_date, p.amount DESC
LIMIT 40