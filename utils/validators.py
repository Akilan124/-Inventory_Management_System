def is_valid_product(name, price, quantity):
    if not name or price < 0 or quantity < 0:
        return False
    return True
