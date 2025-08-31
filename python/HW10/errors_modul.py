class LoadError(Exception):
    pass


def load_data(df):
    if df[df["quantity"] < 1].shape[0] > 0:
        raise LoadError("Количество товара не может быть меньше 1")
    elif df[df["unit_price"] <= 0].shape[0] > 0:
        raise LoadError("Цена товара должна быть больше 0")
    elif df[(df["discount"] < 0) | (df["discount"] > 0.8)].shape[0] > 0:
        raise LoadError("Скидка должна быть в диапазоне от 0 до 0.8")
