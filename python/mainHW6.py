# К задаче №3 основной
from HW6 import f_sum, f_minus, f_mult, f_div
sum = f_sum(6, 7)
print(f'Сумма: {sum}')
minus = f_minus(11, 6)
print(f'Вычитание: {minus}')
mult = f_mult(5, 10)
print(f'Умножение: {mult}')
div = f_div(40,20)
print(f'Деление: {div}')
#1. Напишите программу в модуле main.py, которая запрашивает у пользователя имя и возраст, используя функцию register_user() из модуля users.py. 
# Если возраст меньше 18, программа должна вывести «Доступ ограничен», иначе — «Добро пожаловать, {имя}!». 
# Результат работы функции (имя и возраст) не обязательно сохранять в файл, но можно вернуть как строку и вывести на экран.

from users import register_users
name, age = register_users()
if age < 18:
   print('Доступ ограниен')
else:
    print(f'Добро пожаловать, {name}')
print(name, age)

#2. Создайте программу в модуле main.py, которая с помощью функции calculate_stats(numbers) из модуля stats.py принимает от пользователя строку чисел, 
# преобразует её в список, находит сумму, максимальное и минимальное значение. Если сумма больше 100, выводится сообщение «Большая сумма». 
# Работа с файлами в этой задаче не используется, результаты просто выводятся на экран.
from stats import calculate_stats
num = input('Введите числа через пробела:')
numbers = [int(i) for i in num.split()]
calculate_stats(numbers)

#3. Реализуйте программу в модуле main.py, которая использует функцию make_order(product, qty) из модуля shop.py для оформления заказа. 
# В модуле shop.py хранится словарь с товарами и их ценами. Пользователь вводит название товара и количество, функция проверяет, есть ли такой товар, и если он найден, считает общую стоимость и возвращает строку с информацией о заказе. 
# Если товара нет — возвращается сообщение «Товар не найден». Заказы сохраняются в файл orders.txt.

from shop import make_order
product = input('Введите название товара:').title()
qty = int(input('Введите количество товара:'))
t = make_order(product, qty)
print(t)
try:
    with open('orders.txt', 'a') as file:
        file.write(f'{t} \n') # в файл orders записались символы ромбы а не буквы
except FileNotFoundError:
    print("Файл не найден!")
except PermissionError:
     print("Нет доступа к файлу!")
except IsADirectoryError:
    print("Указан путь к папке, а не к файлу!")
except IOError:
    print("Ошибка ввода-вывода файла!")
except UnicodeDecodeError:
    print("Неправильная кодировка файла!")
finally:
    print("Ошибок нет!")

#4.Напишите программу в модуле main.py, которая вызывает функцию filter_even_numbers(input_file, output_file) из модуля numbers.py. 
# Входной файл содержит числа по одному в строке. Функция должна считать все числа, отфильтровать только чётные и сохранить их в другой файл, 
# а также вернуть количество найденных чётных чисел, которое выводится в консоль.
from numbers_1 import filter_even_numbers
input_file = 'input_file.txt'
output_file = 'output_file.txt'
content = filter_even_numbers(input_file, output_file)
print(f'Количество четных чисел: {content}')

#5.Создайте программу в модуле main.py, которая использует функцию analyze_file(path) из модуля text_analyzer.py. 
# Функция считывает содержимое указанного текстового файла, определяет количество строк, количество слов и самое длинное слово, а затем возвращает эти данные в виде строки. 
# Программа выводит результат в консоль и сохраняет его в файл analysis.txt.
from text_analyzer import analyze_file
path = 'textfileanalyze.txt'
con = analyze_file(path)
print(con)
with open('analysis.txt', 'a', encoding='utf-8') as file:
    file.write(con)