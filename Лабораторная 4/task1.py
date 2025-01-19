if __name__ == "__main__":
    class Animal:
        """ Базовый класс для всех животных. """

        def __init__(self, name: str, age: int):
            """
            Инициализация базового класса Animal.

            :param name: Имя животного.
            :param age: Возраст животного в годах.
            """
            self._name = name  # Непубличный атрибут для инкапсуляции
            self._age = age  # Непубличный атрибут для инкапсуляции

        @property
        def name(self) -> str:
            """ Возвращает имя животного. """
            return self._name

        @property
        def age(self) -> int:
            """ Возвращает возраст животного. """
            return self._age

        def make_sound(self) -> str:
            """ Возвращает звук, который издает животное. """
            return "Some sound"

        def __str__(self) -> str:
            """ Строковое представление животного. """
            return f"{self.__class__.__name__}(name={self.name}, age={self.age})"

        def __repr__(self) -> str:
            """ Официальное строковое представление животного. """
            return f"{self.__class__.__name__}(name={self.name!r}, age={self.age!r})"


    class Dog(Animal):
        """ Класс, представляющий собаку. """

        def __init__(self, name: str, age: int, breed: str):
            """
            Инициализация класса Dog.

            :param name: Имя собаки.
            :param age: Возраст собаки в годах.
            :param breed: Порода собаки.
            """
            super().__init__(name, age)  # Вызов конструктора родительского класса
            self._breed = breed  # Непубличный атрибут для инкапсуляции

        @property
        def breed(self) -> str:
            """ Возвращает породу собаки. """
            return self._breed

        def make_sound(self) -> str:
            """ Возвращает звук, который издает собака. """
            return "Гав!"  # Перегруженный метод

        def __str__(self) -> str:
            """ Строковое представление собаки. """
            return f"{super().__str__()}, breed={self.breed}"

        def __repr__(self) -> str:
            """ Официальное строковое представление собаки. """
            return f"{self.__class__.__name__}(name={self.name!r}, age={self.age!r}, breed={self.breed!r})"


    class Cat(Animal):
        """ Класс, представляющий кошку. """

        def __init__(self, name: str, age: int, color: str):
            """
            Инициализация класса Cat.

            :param name: Имя кошки.
            :param age: Возраст кошки в годах.
            :param color: Цвет кошки.
            """
            super().__init__(name, age)  # Вызов конструктора родительского класса
            self._color = color  # Непубличный атрибут для инкапсуляции

        @property
        def color(self) -> str:
            """ Возвращает цвет кошки. """
            return self._color

        def make_sound(self) -> str:
            """ Возвращает звук, который издает кошка. """
            return "Мяу!"  # Перегруженный метод

        def __str__(self) -> str:
            """ Строковое представление кошки. """
            return f"{super().__str__()}, color={self.color}"

        def __repr__(self) -> str:
            """ Официальное строковое представление кошки. """
            return f"{self.__class__.__name__}(name={self.name!r}, age={self.age!r}, color={self.color!r})"


    # Пример использования классов
    if __name__ == '__main__':
        dog = Dog(name="Рекс", age=5, breed="Бульдог")
        cat = Cat(name="Мурка", age=3, color="Чёрный")

        print(dog)  # Проверка метода __str__
        print(repr(dog))  # Проверка метода __repr__
        print(dog.make_sound())  # Проверка метода make_sound

        print(cat)  # Проверка метода __str__
        print(repr(cat))  # Проверка метода __repr__
        print(cat.make_sound())  # Проверка метода make_sound
    pass
