class Animal:
    def eat(self):
        print(f'{self.__class__.__name__} eats everything...')


class Cat(Animal):
    def meow(self):
        print(f'{self.__class__.__name__} say "meow"')

    def eat(self):
        print(f'{self.__class__.__name__} eats fish...')


class Dog(Animal):
    def bark(self):
        print(f'{self.__class__.__name__} say "woof"')

    def eat(self):
        print(f'{self.__class__.__name__} eats meat...')


class CatDog(Dog, Cat):
    def eat(self):
        print(f'{self.__class__.__name__} eats meat and fish...')


if __name__ == '__main__':
    catdog = CatDog()

    catdog.meow()
    catdog.bark()
    catdog.eat()
    super(CatDog, catdog).eat()
