import time


def decorator(func):
    def wrapper(*args, **kwargs):
        timer = time.time()
        result = func(*args, **kwargs)
        print(f'Функция отработала за время: {time.time() - timer}\nБыли вызваны аргументы:\n{args}\n{kwargs}\nРезультат:{result}')
        return result
    return wrapper


@decorator
def summa(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum


summa(1, 2, 4, 5)
