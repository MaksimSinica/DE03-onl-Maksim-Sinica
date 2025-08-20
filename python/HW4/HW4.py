#1. Создайте список fruits с элементами "apple", "banana", "cherry". Выведите первый элемент списка.
fruits = ['apple', 'banana', 'cherry']
print(fruits[0])

#2. Создайте словарь student с ключами name, age и grade и соответствующими значениями. Выведите значение по ключу name.
student = {'name':'Maxim', 'age':'27', 'grade':'5'}
print(student.get('name'))

#3.  Напишите программу, которая создает множество уникальных слов из введенной пользователем строки. 
# Программа должна учитывать только уникальные слова и игнорировать регистр.
a = input('Введите через пробел слова: ')
word = a.split()
uniq_word = set(word)
print(uniq_word)

