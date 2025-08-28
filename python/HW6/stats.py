def calculate_stats(numbers):
    summa = sum(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    print(f'Сумма: {summa}, Максимум: {maximum}, Минимум: {minimum}')
    if summa > 100:
        print('Большая сумма')