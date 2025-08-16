def make_order(product, qty):
    dict = {'Майка':30, 'Джинсы':95, 'Кеды':67, 'Рубашка':73}
    if product in dict:
        stoim = dict[product] * qty
        return f'Наименование товара: {product}, Количество: {qty}, Общая стоимость: {stoim}'
    else:
        return 'Товар не найден'