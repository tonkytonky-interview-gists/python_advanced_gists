from assertpy import assert_that

from utils.logger import log
from utils.utils import format_header


class SomeClass:
    """
    Методы __new__ и __init__
    """

    def __new__(cls, *args, **kwargs):
        """
        Метод __new__ создаёт экземпляр класса
        """
        log.info("Создать экземпляр класса")

        instance = super().__new__(cls)
        return instance

    def __init__(self, value):
        """
        Метод __init__ заполняет созданный экземпляр
        """
        log.info("Заполнить экземпляр класса")

        self.value = value


class Singleton:
    """
    Реализация Синглтона через метод __new__
    """
    _instance = None  # Хранилище единственного экземпляра

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            log.info("Создать экземпляр только если его ещё нет")
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value=None):
        if not hasattr(self, "field"):
            log.info("Инициализировать только при первом создании")
            self.field = value


class SingletonMeta(type):
    """
    Реализация Синглтона через метакласс
    """
    _instances = {}  # Хранилище экземпляров

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            log.info("Создать экземпляр только если его ещё нет")
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class SingletonFoo(metaclass=SingletonMeta):
    def __init__(self, value=None):
        log.info("Инициализировать только при первом создании")
        self.field = value


class SingletonBar(metaclass=SingletonMeta):
    def __init__(self, value=None):
        log.info("Инициализировать только при первом создании")
        self.field = value


def run__some_class():
    """
    Методы __new__ и __init__
    """

    log.info(format_header(SomeClass.__doc__.strip()))

    some_object = SomeClass(value="some_value")

    description = "Объект создан и заданы параметры"
    assert_that(some_object.value, description=description).is_equal_to("some_value")
    log.info(f"Assert: {description}")


def run__singleton():
    """
    Реализация Синглтона через метод __new__
    """

    log.info(format_header(Singleton.__doc__.strip()))

    log.info("Создать объект 11")
    singleton__1 = Singleton("11")
    singleton__1_value = singleton__1.field

    log.info("Создать объект 22")
    singleton__2 = Singleton("22")
    singleton__2_value = singleton__2.field

    description = "Все вызовы создания возвращают один и тот же объект"
    log.info(f"Assert: {description}")
    assert_that(singleton__1, description=description).is_same_as(singleton__2)

    description = "Значение поля объекта не изменилось"
    log.info(f"Assert: {description}")
    assert_that(singleton__1_value, description=description).is_equal_to(
        singleton__2_value)


def run__singleton_meta():
    """
    Реализация Синглтона через метакласс
    """

    log.info(format_header(SingletonMeta.__doc__.strip()))

    log.info("Создать объект 11 через класс SingletonFoo")
    singleton__1 = SingletonFoo("11")
    log.info("Создать объект 22 через класс SingletonFoo")
    singleton__2 = SingletonFoo("22")

    log.info("Создать объект 33 через класс SingletonBar")
    singleton__3 = SingletonBar("33")
    log.info("Создать объект 44 через класс SingletonBar")
    singleton__4 = SingletonBar("44")

    description = "Все создания объектов через один класс возвращают один и тот же объект"
    log.info(f"Assert: {description}")
    assert_that(singleton__1, description=description).is_same_as(singleton__2)
    assert_that(singleton__3, description=description).is_same_as(singleton__4)

    description = "Создания объектов через разные классы возвращают разные объекты"
    log.info(f"Assert: {description}")
    assert_that(singleton__1, description=description).is_not_same_as(singleton__3)


def main():
    run__some_class()
    run__singleton()
    run__singleton_meta()


if __name__ == "__main__":
    main()
