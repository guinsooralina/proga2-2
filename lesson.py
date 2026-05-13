from abc import ABC, abstractmethod

class OnlineLesson(ABC):
    # Базовый класс с шаблонным методом
    # conduct_lesson - это скелет алгоритма из 7 шагов
    def conduct_lesson(self, topic):
        self.connect_platform()
        self.greet_students()
        self.announce_topic(topic)
        self.main_part(topic)
        self.check_understanding()
        self.give_homework(topic)
        if self.hook_record_lesson():
            self.record_lesson()
        self.say_goodbye()
    
    def connect_platform(self):
        print("Подключение к платформе... Успешно!")
    
    def greet_students(self):
        print("Здравствуйте, ученики!")
    
    def announce_topic(self, topic):
        print(f"Тема сегодняшнего урока: {topic}")
    
    def give_homework(self, topic):
        print(f"Домашнее задание: повторить тему '{topic}' и выполнить упражнения")
    
    def say_goodbye(self):
        print("Урок окончен! До свидания!\n")
    
    def hook_record_lesson(self):
        return False
    
    def record_lesson(self):
        pass
    
    @abstractmethod
    def main_part(self, topic):
        raise NotImplementedError
    
    @abstractmethod
    def check_understanding(self):
        raise NotImplementedError


class SeminarLesson(OnlineLesson):
    
    def main_part(self, topic):
        print(f"Обсуждение темы '{topic}'")
        print("Ученики решают уравнения в онлайн-доске и объясняют свои решения")
        print("Разбор сложных моментов")
    
    def check_understanding(self):
        print("Проверка понимания:")
        print("Учитель отправляет задание в чат, ученики присылают решения в личные сообщения")
        print("Учитель задаёт уточняющие вопросы")
    
    def hook_record_lesson(self):
        return True
    
    def record_lesson(self):
        print("Запись урока сохранена в архив")


seminar = SeminarLesson()
seminar.conduct_lesson("Решение линейных уравнений")
