from functools import wraps


def val_checker(callback):
    @wraps(callback)
    def wrapper(func):
        def hide(*args):
            if not callback(*args):
                raise ValueError(f"Что-то пошло не так:")
            else:
                return func(*args)
        return hide
    return wrapper

@val_checker(lambda x: x > 0)
def calc_cube(x):
    print(f'{x} в кубе  = {x ** 3}')

if __name__ == '__main__':
    calc_cube(2)
    calc_cube(0.5)
    calc_cube(-1)