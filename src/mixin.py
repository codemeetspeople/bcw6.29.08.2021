from abc import ABCMeta


class Number(metaclass=ABCMeta):
    _validator = None

    def __init__(self, value):
        self._value = self._validator(value)

    @property
    def value(self):
        return self._value

    def __str__(self):
        return f'{self.value}'


class Integer(Number):
    _validator = int


class Float(Number):
    _validator = float


class AbsoluteMixin:
    @property
    def absolute_value(self):
        return abs(self.value)


class AbsoluteInteger(Integer, AbsoluteMixin):
    pass


class AbsoluteFloat(Float, AbsoluteMixin):
    pass


if __name__ == '__main__':
    intval = AbsoluteInteger(-10.5)
    floatval = AbsoluteFloat(-10.5)

    print(intval)
    print(floatval)

    print(intval.absolute_value)
    print(floatval.absolute_value)
