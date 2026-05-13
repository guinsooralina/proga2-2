# proga2-2
## Классы:

**AbstractClass**: Абстрактный класс, определяющий скелет алгоритма. Содержит шаблонный метод template_method, который вызывает комбинацию абстрактных методов, конкретных методов и хуков
- **ConcreteClass**: Конкретный класс, который реализует абстрактные методы (required_operations) и может переопределять хуки (hook operations)
- **Client**: Клиентский код, который работает с объектами через интерфейс абстрактного класса

## Базовый паттерн:

<img width="793" height="802" alt="image" src="https://github.com/user-attachments/assets/2503d967-f891-49ae-9e19-edbf11aee4c1" />

**Задача:**

**OnlineLesson** (Абстрактный класс): Определяет скелет проведения онлайн-урока. Содержит шаблонный метод, который вызывает комбинацию абстрактных методов, конкретных методов и хука.

**SeminarLesson** (Конкретный класс): Реализует абстрактные методы (основная часть урока, проверка понимания) и может переопределять хуки.

**Client** (Клиентский код): Создаёт объект SeminarLesson и вызывает его метод conduct_lesson с параметром topic. Работает с объектом через интерфейс абстрактного класса.

**Функционал программы:**

| Элемент схемы              | Код                                      |
|---------------------------|------------------------------------------|
| `AbstractClass`           | `OnlineLesson`                           |
| `templateMethod()`        | `conduct_lesson()`                       |
| `step1()`                 | `connect_platform()`                     |
| `step2()`                 | `greet_students()`                       |
| `step3()`                 | `announce_topic()`                       |
| `step4()`                 | `main_part()`                            |
| `step5()`                 | `check_understanding()`                  |
| `step6()`                 | `give_homework()`                        |
| `step7()`                 | `say_goodbye()`                          |
| `ConcreteClass1`          | `SeminarLesson` (семинарское занятие)    |
| if в шаблонном методе     | `if self.hook_record_lesson(): self.record_lesson()` |

- **`conduct_lesson()`** — Шаблонный метод (скелет из 7 шагов)

- **`connect_platform()` / `greet_students()` / `announce_topic()` / `give_homework()` / `say_goodbye()`** — Конкретные методы (общие для всех)

- **`main_part()` / `check_understanding()`** — Абстрактные методы (обязательны для реализации)

- **`hook_record_lesson()`** — Хук-флаг (включает/выключает запись)

- **`record_lesson()`** — Тело хука (что именно делать)
