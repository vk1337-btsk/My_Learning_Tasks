from datetime import date, datetime, time


def print_birthday():
    """
    Вам доступна дата birthday. Дополните приведенный ниже код, чтобы он вывел следующие её компоненты:

    полное название месяца на английском
    полное название дня недели на английском
    год в формате YYYY
    номер месяца в формате MM
    день месяца в формате DD
    """
    birthday = date(1992, 10, 6)

    print('Название месяца:', birthday.strftime('%B'))
    print('Название дня недели:', birthday.strftime('%A'))
    print('Год:', birthday.strftime('%Y'))
    print('Месяц:', birthday.strftime('%m'))
    print('День:', birthday.strftime('%d'))
#print_birthday()


def print_date_iso_ru_en():
    """
    В переменной florida_hurricane_dates хранится список дат (тип date), в которые произошел ураган во Флориде с
    1950
    1950 по
    2017
    2017 год.

    Дополните приведенный ниже код, чтобы он вывел самую раннюю дату из списка florida_hurricane_dates в трех различных форматах:

    в стандарте ISO (YYYY-MM-DD)
    в типичном для России стиле (DD.MM.YYYY)
    в типичном для Америки стиле (MM/DD/YYYY)
    """
    florida_hurricane_dates = ['08-25-1992', '09-16-1928', '10-18-1924', '07-21-1943', '10-02-1899', '08-13-2004',
        '09-18-1926','08-30-1965', '09-10-1960', '10-24-2005']

    first_date = min(florida_hurricane_dates)

    # конвертируем дату в ISO и RU формат
    iso = 'Дата первого урагана в ISO формате: ' + first_date.isoformat()
    ru = 'Дата первого урагана в RU формате: ' + first_date.strftime('%d.%m.%Y')
    us = 'Дата первого урагана в US формате: ' + first_date.strftime('%m/%d/%Y')

    print(iso)
    print(ru)
    print(us)
#print_date_iso_ru_en()


def print_min_date():
    """
    Напишите программу, которая принимает на вход две даты и выводит ту, что меньше.

    Формат входных данных
    На вход программе подаются две корректные даты в ISO формате (YYYY-MM-DD), каждая на отдельной строке.

    Формат выходных данных
    Программа должна выбрать из двух введенных дат меньшую и вывести ее в формате DD-MM (YYYY).
    """
    year, month, day = map(int, input().split("-"))
    date1 = date(year, month, day)

    date2 = date.fromisoformat(input())

    print(min(date1, date2).strftime("%d-%m (%Y)"))
#print_min_date


def print_sorted_list_date():
    # 5
    # 2021-08-01
    # 2021-08-02
    # 2021-07-01
    # 2021-06-01
    # 2021-05-01
    print(*[d.strftime("%d/%m/%Y") for d in sorted([date.fromisoformat(input()) for el in range(int(input()))])],
          sep="\n")
#print_sorted_list_date()


dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)]
def print_good_dates():
    """
    Тимур считает дату «интересной», если её год совпадает с годом его рождения, а сумма номера месяца и номера дня
    равна его возрасту. Год рождения Тимура — 1992, возраст — 29 лет.

    Реализуйте функцию print_good_dates(), которая принимает один аргумент:

    dates — список дат (тип date)
    Функция должна выводить «интересные» даты в порядке возрастания, каждую на отдельной строке, в формате
    month_name DD, YYYY, где month_name — полное название месяца на английском.

    Примечание 1. Если в функцию передается пустой список или список без интересных дат, функция ничего
    не должна выводить.

    Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию print_good_dates(),
    но не код, вызывающий ее.
    """
    if dates == []:
        return
    my_dates = [el for el in dates if el.year == 1992 and el.month + el.day == 29]
    if my_dates == []:
        return
    return print(*[el.strftime("%B %d, %Y") for el in sorted(my_dates)], sep="\n")
#print_good_dates


day, month, year = 31, 12, 2021
def is_correct(day, month, year):
    try:
        my_date = date(year, month, day)
        return True
    except:
        return False


def print_min_raznost():
    """
    Ученики онлайн-школы BEEGEEK решили выяснить, кто из них быстрее всех решит домашнее задание по математике. Для
    этого каждый ученик зафиксировал время начала и окончания решения своей домашней работы.

    Вам доступен словарь data, содержащий результаты учеников. Ключом в словаре является имя ученика, а значением —
    кортеж, первый элемент которого — время начала решения, второй элемент — время окончания решения. Дополните
    приведенный ниже код, чтобы он вывел имя ученика, который затратил на решение домашнего задания меньше всего
    времени.

    Примечание 1. Гарантируется, что искомый ученик единственный.

    Примечание 2. Дата-времена в кортежах представлены в виде строк в формате DD.MM.YYYY HH:MM:SS.
    """
    data = {'Дима': ('03.11.2021 09:31:18', '03.11.2021 11:41:28'),
            'Геор': ('01.11.2021 09:03:04', '01.11.2021 12:40:35'),
            'Анна': ('02.11.2021 04:41:54', '02.11.2021 05:39:40'),
            'Илина': ('02.11.2021 01:36:40', '02.11.2021 04:48:27'),
            'Герман': ('04.11.2021 07:51:19', '04.11.2021 09:53:53'),
            'Руслан': ('01.11.2021 11:26:06', '01.11.2021 12:56:24'),
            'Лера': ('03.11.2021 11:09:41', '03.11.2021 14:37:41'),
            'Егор': ('03.11.2021 05:29:38', '03.11.2021 06:01:59'),
            'Максим': ('05.11.2021 13:05:03', '05.11.2021 14:27:41'),
            'Саша': ('03.11.2021 04:14:26', '03.11.2021 05:10:58'),
            'Марина': ('05.11.2021 15:21:06', '05.11.2021 18:33:46')}

    min_data = {key: datetime.strptime(value[1], "%d.%m.%Y %H:%M:%S") - datetime.strptime(value[0], "%d.%m.%Y %H:%M:%S")
                for key, value in data.items()}

    print(min(min_data, key=lambda key: min_data[key]))
#print_min_raznost()


def read_file_diary_and_sorted():
    """
    Вам доступен текстовый файл diary.txt, в который космонавт записывал небольшие отчёты за день. Каждый новый отчёт он
     мог записать либо в начало файла, либо в середину, либо в конец. Все отчеты разделены между собой пустой строкой.
     Каждый новый отчёт начинается со строки с датой и временем в формате DD.MM.YYYY; HH:MM, после которой следуют
     события, произошедшие за указанный день:

    29.04.2006; 06:55
    It wasn’t until several hours after launch that we were able to take the time to get out of our seats and enter the
    “habitation module.”
    Then, after another orbital maneuver, we finally were able to take a several hour break and get a little sleep.

    03.05.2006; 20:24
    Everybody had a sleeping bag although I only used mine on a couple of brief occasions, and then only when getting a
    little chilly.

    ...
    Напишите программу, которая расставляет все записи космонавта в хронологическом порядке и выводит полученный
     результат.
    """
    with open("1.6.1   diary.txt", "r", encoding="utf-8") as file:
        my_dict = {datetime.strptime(t[:17], "%d.%m.%Y; %H:%M"): t for t in file.read().split("\n\n")}
        print("\n\n".join([my_dict[k] for k in sorted(my_dict.keys())]))
    return
#read_file_diary_and_sorted()

def check_dates_free_or_broned_in_hotels(dates, some_date):
        # Если бронируют период
        if "-" in some_date:
            some_date1, some_date2 = map(lambda d: datetime.strptime(d, "%d.%m.%Y").date(), some_date.split("-"))
            for d in dates:
                if "-" in d:
                    d1, d2 = map(lambda d: datetime.strptime(d, "%d.%m.%Y").date(), d.split("-"))
                    if (d1 <= some_date1 and some_date1 <= d2) or (d1 <= some_date2 and some_date2 <= d2) or (
                            some_date1 <= d1 and d2 <= some_date2):
                        return False
                else:
                    d = datetime.strptime(d, "%d.%m.%Y").date()
                    if some_date1 <= d and d <= some_date2:
                        return False

        else:
            some_date = datetime.strptime(some_date, "%d.%m.%Y").date()

            for d in dates:
                if "-" in d:
                    d1, d2 = map(lambda d: datetime.strptime(d, "%d.%m.%Y").date(), d.split("-"))
                    if d1 <= some_date and some_date <= d2:
                        return False
                else:
                    d = datetime.strptime(d, "%d.%m.%Y").date()
                    if d == some_date:
                        return False
        return True
#dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
#some_date = '14.11.2021-22.11.2021'
#print(check_dates_free_or_broned_in_hotels(dates, some_date))