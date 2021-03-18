from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        for arg in args:
            print(f'{func.__name__}({arg}: {type(arg)})')
        return result
    return wrapper


@type_logger
def calc_cube(*args):
    for arg in args:
        print(f'{arg} в кубе  = {arg ** 3}')

if __name__ == '__main__':
    calc_cube(5, 3, 2.5)
