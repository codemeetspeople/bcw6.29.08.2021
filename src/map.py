def increment(x):
    return x + 1


def pow2(x):
    return x ** 2


def handler(func, sequence):
    result = []

    for elem in sequence:
        result.append(func(elem))
    return result


if __name__ == '__main__':  # pragma: no cover
    source = [1, 2, 3, 4, 5]

    print(source)
    print(handler(increment, source))
    print(handler(pow2, source))
