# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

from pydoc import ModuleScanner


students = [
    {"first_name": "Вася"},
    {"first_name": "Петя"},
    {"first_name": "Маша"},
    {"first_name": "Маша"},
    {"first_name": "Петя"},
]
# # ???
# from collections import Counter
# all_values = []
# for dictionary in students:
#     all_values.extend(dictionary.values())

# for name in all_values:
# print(f'Вася: {all_values.count('Вася')}')
# print(f'Петя: {all_values.count('Петя')}')
# print(f'Маша: {all_values.count('Маша')}')

# # Задание 2
# # Дан список учеников, нужно вывести самое часто повторящееся имя
# # Пример вывода:
# # Самое частое имя среди учеников: Маша
students = [
    {"first_name": "Вася"},
    {"first_name": "Петя"},
    {"first_name": "Маша"},
    {"first_name": "Маша"},
    {"first_name": "Оля"},
]
# ???
# Соберем все имена из списка:
# names = []
# for students in students:
#     names.append(students['first_name'])


# Подсчитываем колличество вхождений:
# name_counts = {}
# for name in names:
#     if name in name_counts:
#         name_counts[name] +=1
#     else:
#         name_counts[name] = 1
# most_frequent_name = max(name_counts, key= name_counts.get)
# print(f'Самое частое имя среди учеников: {most_frequent_name}')

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {"first_name": "Вася"},
        {"first_name": "Вася"},
    ],
    [  # это – второй класс
        {"first_name": "Маша"},
        {"first_name": "Маша"},
        {"first_name": "Оля"},
    ],
    [  # это – третий класс
        {"first_name": "Женя"},
        {"first_name": "Петя"},
        {"first_name": "Женя"},
        {"first_name": "Саша"},
    ],
]
# ???
# Пройти по каждому классу в списке school_students.
# Для каждого класса подсчитать частоту имён.
# Найти самое частое имя в текущем классе.
# Вывести результат с номером класса.


# Для этого используем цикл (повторяем одно и то же для каждого словаря в спике.
# Для получения словарей с индексами используем enumirate().
# С помощью нейросетки додумался начинать индекс с единицы, а не с 0 (для более удобного отображения номера класса)

for class_idx, class_students in enumerate(school_students, start=1): # Элемент и его индекс
    # Собираем имена учеников текущего класса
    names = []
    for student in class_students:
        names.append(student["first_name"])

    # Подсчитываем количество повторений каждого имени, как в прошлом задании.
    name_counts = {}
    for name in names:
        if name in name_counts:
            name_counts[name] += 1
        else:
            name_counts[name] = 1

    # Поиск самого частого имени в классе:
    most_frequent_name = max(name_counts, key=name_counts.get)

    # Выводим самое частое имя в классе:
    print(f"Самое частое имя среди учеников: {most_frequent_name}")

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0
# Класс 2б: девочки 0, мальчики 2

school = [
    {"class": "2a", "students": [{"first_name": "Маша"}, {"first_name": "Оля"}]},
    {"class": "2б", "students": [{"first_name": "Олег"}, {"first_name": "Миша"}]},
    {
        "class": "2в",
        "students": [
            {"first_name": "Даша"},
            {"first_name": "Олег"},
            {"first_name": "Маша"},
        ],
    },
]
is_male = {
    "Олег": True,
    "Маша": False,
    "Оля": False,
    "Миша": True,
    "Даша": False,
}
# ???


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {"class": "2a", "students": [{"first_name": "Маша"}, {"first_name": "Оля"}]},
    {"class": "3c", "students": [{"first_name": "Олег"}, {"first_name": "Миша"}]},
]
is_male = {
    "Маша": False,
    "Оля": False,
    "Олег": True,
    "Миша": True,
}
# ???
