from abc import ABC, abstractmethod

class AbstractClass(ABC):
    """Абстрактный класс с шаблонным методом"""
    def template_method(self):
        """
        Шаблонный метод, определяющий скелет алгоритма.
        Вызывает базовые операции, абстрактные методы (обязательные для подклассов) и хуки (опционально).
        """
        self.base_operation1()
        self.required_operations1()  # Обязательно реализовать в подклассе
        self.base_operation2()
        self.hook1()  # Опционально переопределить
        self.required_operations2()  # Обязательно реализовать в подклассе
        self.base_operation3()
        self.hook2()  # Опционально переопределить

    def base_operation1(self):
        print("AbstractClass says: I am doing the bulk of the work")

    def base_operation2(self):
        print("AbstractClass says: But I let subclasses override some operations")

    @abstractmethod
    def required_operations1(self):
        pass

    @abstractmethod
    def required_operations2(self):
        pass

    def hook1(self):
        print("Overridden Hook1")

    def hook2(self):
        print("Hook2")

class ConcreteClass1(AbstractClass):
    """
    Конкретные классы должны реализовать все абстрактные операции базового класса.
    Они также могут переопределить некоторые операции с реализацией по умолчанию.
    """
    def required_operations1(self):
        print("Implemented Operation1")

    def required_operations2(self):
        print("Implemented Operation2")

class ConcreteClass2(AbstractClass):
    """
    Конкретные классы должны реализовать все абстрактные операции базового класса.
    Они также могут переопределить некоторые операции с реализацией по умолчанию.
    """
    def required_operations1(self):
        print("Implemented Operation1")

    def required_operations2(self):
        print("Implemented Operation2")

# Клиентский код
def client_code(abstract_class: AbstractClass):
    abstract_class.template_method()

if __name__ == "__main__":
    print("Same client code can work with different subclasses:")
    client_code(ConcreteClass1())
    print("")
    client_code(ConcreteClass2())
