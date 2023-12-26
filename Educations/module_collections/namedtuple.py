from collections import namedtuple
import csv
import datetime


def task_namedtuple_animal():
    """
    Вам доступен именованный кортеж Animal, который содержит данные о животном. Первым элементом именованного кортежа
    является имя животного, вторым — семейство, третьим — пол, четвертым — цвет. Также доступен файл data.pkl,
    содержащий сериализованный список таких кортежей.

    Дополните приведенный ниже код, чтобы для каждого кортежа из этого списка он вывел названия его полей и значения
    этих полей в следующем формате:
    name: <значение>
    family: <значение>
    sex: <значение>
    color: <значение>
    Между полями и значениями двух разных кортежей должна располагаться пустая строка.

    Примечание 1. Сначала должно следовать содержание первого кортежа из списка, затем второго, и так далее.

    Примечание 2. Например, если бы файл data.pkl содержал следующий сериализованный список:

    [Animal(name='Alex', family='dogs', sex='m', color='brown'), Animal(name='Nancy', family='dogs', sex='w',
    color='black')]
    то программа должна была бы вывести:

    name: Alex
    family: dogs
    sex: m
    color: brown

    name: Nancy
    family: dogs
    sex: w
    color: black
    """
    Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])

    with open("data.pkl", 'rb') as file:
        animals = pickle.load(file)
        for animal in animals:
            for field, value in zip(Animal._fields, animal):
                print(f"{field}: {value}")
            print()


def task_namedtuple_user():
    """
    Вам доступен именованный кортеж User, который содержит данные о пользователе некоторого ресурса. Первым элементом
    именованного кортежа является имя пользователя, вторым — фамилия, третьим — адрес электронной почты, четвертым —
    статус оформленной подписки. Также доступен список users, содержащий эти кортежи.

    Дополните приведенный ниже код, чтобы он вывел данные о каждом пользователе из этого списка, предварительно
    отсортировав их по статусу подписки от дорогой к дешевой, а при совпадении статусов — в лексикографическом порядке
    адресов электронных почт. Данные о каждом пользователе должны быть указаны в следующем формате:

    <имя> <фамилия>
      Email: <адрес электронной почты>
      Plan: <статус подписки>
    Между данными двух разных пользователей должна располагаться пустая строка.

    Примечание 1. Самой дорогой подпиской считается Gold, затем Silver, Bronze и Basic.

    Примечание 2. Начальная часть ответа выглядит так (в качестве отступов используйте два пробела):

    Kathleen Lyons
      Email: balchen@att.net
      Plan: Gold

    William Townsend
      Email: kosact@verizon.net
      Plan: Gold
    ...
    """
    User = namedtuple('User', ['name', 'surname', 'email', 'plan'])

    users = [User('Mary', 'Griffin', 'sonnen@yahoo.com', 'Basic'),
             User('Brenda', 'Young', 'retoh@outlook.com', 'Silver'),
             User('Kathleen', 'Lyons', 'balchen@att.net', 'Gold'),
             User('Pamela', 'Hicks', 'corrada@sbcglobal.net', 'Silver'),
             User('William', 'Townsend', 'kosact@verizon.net', 'Gold'),
             User('Clayton', 'Morris', 'berserk@yahoo.com', 'Silver'),
             User('Dorothy', 'Dennis', 'sequin@live.com', 'Gold'),
             User('Tyler', 'Walker', 'noahb@comcast.net', 'Basic'),
             User('Joseph', 'Moore', 'ylchang@sbcglobal.net', 'Silver'),
             User('Kenneth', 'Richardson', 'tbusch@me.com', 'Bronze'),
             User('Stephanie', 'Bush', 'neuffer@live.com', 'Gold'),
             User('Gregory', 'Hughes', 'juliano@att.net', 'Basic'),
             User('Tracy', 'Wallace', 'sblack@me.com', 'Silver'),
             User('Russell', 'Smith', 'isaacson@comcast.net', 'Bronze'),
             User('Megan', 'Patterson', 'hoangle@outlook.com', 'Basic')]

    func_print = lambda u: f"""{u[User._fields[0]]} {u[User._fields[1]]}\n  \
    {User._fields[2].capitalize()}: {u[User._fields[2]]}\n  \
    {User._fields[3].capitalize()}: {u[User._fields[3]]}"""

    func_sorted = lambda u: sorted(sorted(u, key=lambda x: x[2]),
                                   key=lambda x: ["Gold", "Silver", "Bronze", "Basic"].index(x[3]))

    print(*[func_print(user._asdict()) for user in func_sorted(users)], sep="\n\n")


def who_are_you():
    """
    У Тимура имеется немало друзей из других городов или стран, которые часто приезжают к нему в гости с целью
    увидеться и развлечься. Чтобы не забыть ни об одной встрече, Тимур записывает имена и фамилии друзей в csv файл,
    дополнительно указывая для каждого дату и время встречи. Вам доступен этот файл, имеющий название meetings.csv,
    в котором в первом столбце записана фамилия, во втором — имя, в третьем — дата в формате DD.MM.YYYY,
    в четвертом — время в формате HH:MM:

    surname,name,meeting_date,meeting_time
    Харисов,Артур,15.07.2022,17:00
    Геор,Гагиев,14.12.2022,18:00
    ...
    Напишите программу, которая выводит фамилии и имена друзей Тимура, предварительно отсортировав их по дате и времени
    встречи от самой ранней до самой поздней. Фамилии и имена должны быть расположены каждые на отдельной строке.

    Примечание 1. Начальная часть ответа выглядит так:

    Гудцев Таймураз
    Харисов Артур
    Базиев Герман
    ...
    Примечание 2. Гарантируется, что никакие две встречи не имеют одновременно одинаковые даты и время.

    Примечание 3. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.

    Примечание 4. Разделителем в файле meetings.csv является запятая, при этом кавычки не используются.

    Примечание 5. При открытии файла используйте явное указание кодировки UTF-8.
    """
    with open('meetings.csv', encoding="utf-8") as file:
        data = [row for row in csv.DictReader(file)]

        func_data = lambda date_, time_: datetime.strptime(date_ + " " + time_, "%d.%m.%Y %H:%M")

        func_surname_and_name = lambda f, n: f + " " + n

        print(*[func_surname_and_name(el['surname'], el['name']) for el in
                sorted(data, key=lambda d: func_data(d['meeting_date'], d['meeting_time']))], sep="\n")


