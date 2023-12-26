import sys
import pickle
from collections import namedtuple, defaultdict
import csv
from datetime import datetime


"""func.pkl
Hello,
how
are
you
today?"""
def my_func_from_pickle():
    func_file, *args = [a.strip() for a in sys.stdin]

    with open(func_file, 'rb') as file:
        func_file = pickle.load(file)
        print(func_file(*args))
#my_func_from_pickle()


def filter_dump(filename, objects, typename):
    data = [el for el in objects if isinstance(el, typename)]
    with open(filename, "wb") as file:
        pickle.dump(data, file)
    return
#filter_dump('numbers.pkl', [1, '2', 3, 4, '5'], int)


def check_sum(filename, check_summa):
    func = lambda x_check, x_check_summa: "Контрольные суммы совпадают" if x_check == x_check_summa else \
        "Контрольные суммы не совпадают"
    with open(filename, "rb") as file:
        objects = pickle.load(file)
        if isinstance(objects, dict):
            check = sum([el for el in list(objects.keys()) if isinstance(el, int)])
        else:
            check = min([el for el in objects if isinstance(el, int)], default=0) * max(
                [el for el in objects if isinstance(el, int)], default=0)
    return func(check, check_summa)
#filename = input()
#check_summa = int(input())
#print(check_sum(filename, check_summa))


Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])
def my_func():
    with open("data.pkl", 'rb') as file:
        animals = pickle.load(file)
        for animal in animals:
            for field, value in zip(Animal._fields, animal):
                print(f"{field}: {value}")
            print()
#my_func()


def my_func2():
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
#my_func2()


def my_func3():
    with open('meetings.csv', encoding="utf-8") as file:
        data = [row for row in csv.DictReader(file)]

        func_data = lambda date_, time_: datetime.strptime(date_ + " " + time_, "%d.%m.%Y %H:%M")

        func_surname_and_name = lambda f, n: f + " " + n

        print(*[func_surname_and_name(el['surname'], el['name']) for el in
                sorted(data, key=lambda d: func_data(d['meeting_date'], d['meeting_time']))], sep="\n")
#my_func3()


print(defaultdict.fromkeys(['name', 'surname', 'hobby'], None))