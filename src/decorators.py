from typing import Callable

from map import increment


def run_5_times(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        for i in range(5):
            func(*args, **kwargs)

    return wrapper


def run_N_times(times: int) -> Callable:
    def outer_wrapper(func):
        def inner_wrapper(*args, **kwargs):
            for i in range(times):
                func(*args, **kwargs)

        return inner_wrapper
    return outer_wrapper


def parametrize(arg_names: str, values_list: list) -> Callable:
    def decorator(func):
        def wrapper(*args, **kwargs):
            func_args = [elem.strip() for elem in arg_names.split(',')]
            for values in values_list:
                parameters = dict(zip(func_args, values))
                print(f'Call {func.__name__} with {parameters}')
                func(**parameters)
        return wrapper
    return decorator


@parametrize('given, expected', [
    (10, 11), (-10, -9), (0, 1)
])
def test_increment(given, expected):
    assert increment(given) == expected


@run_5_times
def hello(username):
    print(f'Hello, {username}!')


@run_N_times(10)
def hello2(username):
    print(f'Aloha, {username}!')


if __name__ == '__main__':
    test_increment(None, None)
    # hello2('caiman')
    # hello('caiman')
