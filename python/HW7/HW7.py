# 1.Напишите функцию, которая принимает список чисел и возвращает их среднее значение.
# Обработайте исключения, связанные с пустым списком и некорректными типами данных.
def avg_list(lst):
    average_l = sum(lst) / len(lst)
    print(average_l)


try:
    lst_inp = input("Введи числа через пробел: ")
    lst = [int(i) for i in lst_inp.split()]
    avg_list(lst)
except TypeError:
    print("Некорректный тип данных")
except ZeroDivisionError:
    print("Деление на ноль. Список пустой")

# 2. Создайте программу, которая считывает список чисел из файла,
# проверяет каждое число на чётность и записывает результаты (чётное или нечётное) в другой файл.
# Используйте обработку исключений для возможных ошибок ввода-вывода.
try:
    with open(r"HW7\num_list.txt", "r+", encoding="utf-8") as file:
        lst = file.readlines()
        for i in lst:
            file1 = open(r"HW7\output_num_list.txt", "a+", encoding="utf-8")
            if int(i) % 2 == 0:
                file1.write(f"Четное число: {i}")
            else:
                file1.write(f"Нечетное число: {i}")
            file1.close()
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
else:
    print("Файл успешно прочитан!")
finally:
    print("Завершение обработки файла.")


# 1. Создайте программу, которая запрашивает у пользователя список чисел, введённых через пробел, и сохраняет их в список; напишите функцию,
# которая перебирает этот список в цикле и вычисляет квадрат каждого числа, но если встречается отрицательное число, выбрасывается собственное
# исключение NegativeNumberError с сообщением «Отрицательные числа недопустимы», при этом программа должна обработать это исключение,
# вывести сообщение об ошибке и продолжить обработку остальных элементов, а в конце вывести итоговый список квадратов всех корректных чисел.
class NegativeNumberError(Exception):
    pass


def check_value(value):
    if value < 0:
        raise NegativeNumberError("Отрицательные числа недопустимы!")


lst = input("Введите числа через пробел: ").split()


def funct(lst):
    list = []
    for i in lst:
        try:
            value = int(i)
            check_value(value)
        except NegativeNumberError as e:
            print(e)
        else:
            sqr = int(i) ** 2
            list.append(sqr)
    print(list)


funct(lst)
# 2. Создайте программу, которая запрашивает у пользователя пары «ключ:значение», введённые через запятую, и сохраняет их в словарь;
# напишите функцию, которая в цикле проходит по словарю и проверяет, чтобы все значения были положительными числами, при этом если встречается
# отрицательное число или строка вместо числа, выбрасывается собственное исключение InvalidValueError с сообщением «Некорректное значение для
# ключа <ключ>», программа должна обработать это исключение, вывести предупреждение и продолжить проверку остальных элементов, а в конце вывести
# словарь только с корректными данными.


class InvalidValueError(Exception):
    pass


def error(key, value):
    if value < 0:
        raise InvalidValueError(f"Некорректное значение для ключа {key}")


d = {}
key_value = input("Введите через запятую ключ:значение:   ").split(",")
for kv in key_value:
    try:
        key, value = kv.strip().split(":")
        d[key.strip()] = int(value.strip())
    except ValueError:
        print(f"Строка вместо числа для ключа {key}")
print(f"Исходный словарь:  {d}")

d_output = {}


def func_dict(d):
    for key, value in d.items():
        try:
            error(key, value)
        except InvalidValueError as e:
            print(e)
        else:
            d_output[key] = value
    print(f"Словарь с коррекными данными: {d_output}")


func_dict(d)


# 3. Создайте программу, которая запрашивает у пользователя число и с помощью цикла считает факториал этого числа,
# при этом если пользователь вводит отрицательное значение, должно выбрасываться собственное исключение NegativeFactorialError
# с сообщением «Факториал отрицательных чисел не определён», программа должна обработать это исключение и вывести сообщение об ошибке,
# а при корректном вводе — напечатать результат вычисления факториала.
class NegativeFactorialError(Exception):
    pass


def errorneg(n):
    if n < 0:
        raise NegativeFactorialError("Факториал отрицательных чисел не определён!")


try:
    n = int(input("Введите число:  "))
    errorneg(n)
    res = 1
    for i in range(1, n + 1):
        res *= i
    print(f"Факториал числа {n} равен:  {res}")
except NegativeFactorialError as e:
    print(e)
