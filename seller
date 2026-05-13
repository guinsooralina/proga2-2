from abc import ABC, abstractmethod

class SalesTemplate(ABC):
    # Базовый класс с шаблонным методом
    # serve_customer - это скелет алгоритма из 5 шагов
    def serve_customer(self, request):
        self.greet()
        self.identify_needs(request)
        self.offer_upsell(request)
        self.ask_loyalty_card()
        if self.hook_after_card():      # хук: можно включить/выключить бонус
            self.after_card_bonus()
        self.say_goodbye()
    
    def greet(self):
        print("Здравствуйте!")
    
    def say_goodbye(self):
        print("Приходите сново! До свидания! \n")
    
    # хук (по умолчанию выключен, можно переопределить в наследнике)
    def hook_after_card(self):
        return False
    
    # тело хука (по умолчанию пустое, можно переопределить)
    def after_card_bonus(self):
        pass
    
    # абстрактные методы (обязательно реализовать в наследнике)
    @abstractmethod
    def identify_needs(self, request):
        raise NotImplementedError
    
    @abstractmethod
    def offer_upsell(self, request):
        raise NotImplementedError
    
    @abstractmethod
    def ask_loyalty_card(self):
        raise NotImplementedError


class Seller(SalesTemplate):
    # Конкретный класс: реализует абстрактные методы и переопределяет хук
    
    def identify_needs(self, request):
        print(f"Запрос: {request}")
        if "джинсы" in request.lower():
            print("Уточнение: размер, фасон, цвет")
        elif "куртка" in request.lower():
            print("Уточнение: сезон, размер, капюшон")
        else:
            print("Уточнение: размер, цвет")
    
    def offer_upsell(self, request):
        print("Дополнительная продажа:")
        if "джинсы" in request.lower():
            print("- Ремень, футболка")
        elif "куртка" in request.lower():
            print("- Шапка, шарф")
        else:
            print("- Аксессуары")
    
    def ask_loyalty_card(self):
        print("Карта покупателя?")
    
    # переопределяем хук: включаем бонус после карты
    def hook_after_card(self):
        return True
    
    # переопределяем тело хука
    def after_card_bonus(self):
        print("Подарок за оформление карты")


seller = Seller()
seller.serve_customer("хочу джинсы")
seller.serve_customer("нужна куртка")
