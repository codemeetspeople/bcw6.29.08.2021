from typing import Generator


def ari_prog(start: int, stop: int, step: int = 1) -> Generator:
    while start < stop:
        yield start

        start += step


if __name__ == '__main__':  # pragma: no cover
    for i in ari_prog(0, 10, 2):
        print(i)

    gen = ari_prog(0, 10, 2)

    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))

    try:
        print(next(gen))
    except StopIteration:
        print('it\'s time to stop')
