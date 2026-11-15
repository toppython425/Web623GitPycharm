def add(a, b):
    return a + b


def product(a, b):
    """
    :param a:
        num1
    :param b:
        num2
    :return:
        num1 * num2
    """
    return a * b


def multiply(a, b):
    return a ** b


def divide(a, b):
    if b != 0:
        return a / b
    raise ZeroDivisionError('На ноль делить нельзя!')
