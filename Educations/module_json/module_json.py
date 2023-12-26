import json
import csv
from datetime import datetime, time


def print_json_with_indent_sortkeys_separators():
    countries = {'Monaco': 'Monaco', 'Iceland': 'Reykjavik', 'Kenya': 'Nairobi', 'Kazakhstan': 'Nur-Sultan',
                 'Mali': 'Bamako', 'Colombia': 'Bogota', 'Finland': 'Helsinki', 'Costa Rica': 'San Jose',
                 'Cuba': 'Havana', 'France': 'Paris', 'Gabon': 'Libreville', 'Liberia': 'Monrovia',
                 'Angola': 'Luanda', 'India': 'New Delhi', 'Canada': 'Ottawa', 'Australia': 'Canberra'}
    print(json.dumps(countries, indent="   ", sort_keys=True, separators=(",", " - ")))
    return
#print_json_with_indent_sortkeys_separators()


def print_json_with_skipkeys():
    words = {
             frozenset(["tap", "telephone"]): ("tæp", "telifəun"),
             "travel": "trævl",
             ("hello", "world"): ("həˈləʊ", "wɜːld"),
             "moonlight": "muːn.laɪt",
             "sunshine": "ˈsʌn.ʃaɪn",
             ("why", "is", "so", "difficult"): ("waɪ", "ɪz", "səʊ", "ˈdɪfɪkəlt"),
             "adventure": "ədˈventʃər",
             "beautiful": "ˈbjuːtɪfl",
             frozenset(["spoon", "block"]): ("spu:n", "blɔk"),
             "bicycle": "baisikl",
             ("pilot", "fly"): ("pailət", "flai")
            }
    data_json = json.dumps(words, skipkeys=True)
    return print(data_json)
#print_json_with_skipkeys()


def create_json_file():
    club1 = {"name": "FC Byern Munchen", "country": "Germany", "founded": 1900,
             "trainer": "Julian Nagelsmann", "goalkeeper": "M. Neuer", "league_position": 1}

    club2 = {"name": "FC Barcelona", "country": "Spain", "founded": 1899,
             "trainer": "Xavier Creus", "goalkeeper": "M. Ter Stegen", "league_position": 7}

    club3 = {"name": "FC Manchester United", "country": "England", "founded": 1878,
             "trainer": "Michael Carrick", "goalkeeper": "D. De Gea", "league_position": 8}

    with open("data_clubs.json", "w", encoding="utf-8") as file:
        data = json.dump([club1, club2, club3], file, indent="   ")
#create_json_file()

def create_json_file2():
    specs = {
             'Модель': 'AMD Ryzen 5 5600G',
             'Год релиза': 2021,
             'Сокет': 'AM4',
             'Техпроцесс': '7 нм',
             'Ядро': 'Cezanne',
             'Объем кэша L2': '3 МБ',
             'Объем кэша L3': '16 МБ',
             'Базовая частота': '3900 МГц'
            }
    specs_json = json.dumps(specs, indent="   ", ensure_ascii=False)
    print(specs_json)
#create_json_file2()


data = '{"name": "Barsik", "age": 7, "meal": "Wiskas"}'
def is_correct_json(string):
    try:
        data1 = json.loads(string)
        return True
    except:
        return False
#print(is_correct_json(data))
#print(is_correct_json('number = 17'))


data = '{"size": 36, "style": "bold", "name": "text1", "alignment": "center"}'
#data = sys.stdin.read()
def print_dict_from_json(string):
    data = json.loads(string)
    for k, v in data.items():
        print(f'{k}: {", ".join(map(str,v)) if isinstance(v, list) else str(v)}')
    return
#print_dict_from_json(data)


def read_and_editor_json_file():
    with open("data.json", encoding="utf-8") as file:
        data = json.load(file)
        my_data = []
        for d in data:
            if isinstance(d, str):
                my_data.append(d + "!")
            elif d in [True, False]:
                my_data.append(not d)
            elif isinstance(d, int):
                my_data.append(d+1)
            elif isinstance(d, list):
                my_data.append(d + d)
            elif isinstance(d, dict):
                d.update({"newkey": None})
                my_data.append(d)
    with open("updated_data.json", "w", encoding="utf-8") as file:
        json.dump(my_data, file, indent="   ")
#read_and_editor_json_file()


def combining_json():
    with open("data1.json", encoding="utf-8") as file1, open("data2.json", encoding="utf-8") as file2:
        data1 = json.load(file1)
        data2 = json.load(file2)
        data1.update(data2)
    with open("data_merge.json", "w", encoding="utf-8") as file3:
        json.dump(data1, file3, indent="   ")
#combining_json()


def add_key_in_json():
    with open("people.json", encoding="utf-8") as file1, open("updated_people.json", "w", encoding="utf-8") as file2:
        data = json.load(file1)
        my_set_keys = set()
        for d in data:
            my_set_keys = my_set_keys | set(d.keys())

        for d in data:
            for s in list(my_set_keys):
                if s not in d.keys():
                    d[s] = None
        json.dump(data, file2, indent="   ")
#add_key_in_json()


def religion():
    with open("countries.json", encoding="utf-8") as file1, open('religion.json', "w", encoding="utf-8") as file2:
        data = json.load(file1)
        set_religion = set(el["religion"] for el in data)
        my_dict = { el: [] for el in set_religion}
        for d in data:
            my_dict[d['religion']].append(d['country'])
        json.dump(my_dict, file2, indent="   ")
#religion()


def from_csv_to_json():
    with open("playgrounds.csv", encoding="utf-8") as file1, open("addresses.json", "w", encoding="utf-8") as file2:
        data = csv.DictReader(file1, delimiter=";")
        data = [row for row in data]
        my_dict = {}
        for d in data:
            my_dict.setdefault(d['AdmArea'], {}).setdefault(d['District'], []).append(d['Address'])
        json.dump(my_dict, file2, indent="  ", ensure_ascii=False)
#from_csv_to_json()


def filter_students():
    with open('students.json', encoding="utf-8") as file1, open("data.csv", "w", encoding="utf-8", newline="") as file2:
        data = [row for row in json.load(file1)]
        names = [list(data[0].keys())[0], list(data[0].keys())[4]]
        my_data = sorted([{list(el.keys())[0]:list(el.values())[0], list(el.keys())[4]:list(el.values())[4]} for el in data
                   if el['age'] >= 18 and el['progress'] >= 75], key=lambda x: x["name"])
        writer = csv.DictWriter(file2, fieldnames=names, delimiter=",")
        writer.writeheader()
        writer.writerows(my_data)
#filter_students()


def pools():
    with open("pools.json", encoding="utf-8") as file:
        data = [row for row in json.load(file) if row]

        my_time = lambda x: (
                datetime.strptime(x.split("-")[0], "%H:%M").time() <= time(10, 0, 0)
                and datetime.strptime(x.split("-")[1], "%H:%M").time() >= time(12, 0, 0))

        max_lenght_pool = max([(el['DimensionsSummer']['Length'], el['DimensionsSummer']['Width']) for el in data
                               if my_time(el['WorkingHoursSummer']['Понедельник'])], key=lambda x: (x[0], x[1]))

        my_data = [d for d in data if d['DimensionsSummer']['Length'] == max_lenght_pool[0]
                   and d['DimensionsSummer']['Width'] == max_lenght_pool[1]][0]
        print(f"{str(my_data['DimensionsSummer']['Length'])}x{str(my_data['DimensionsSummer']['Width'])}\n{my_data['Address']}")
#pools()


def exam_result():
    with open("exam_results.csv", encoding="utf-8") as file1, open("best_scores.json", "w", encoding="utf-8") as file2:
        data_ = [row for row in csv.DictReader(file1)]

        func_dict_additem = lambda row: dict(zip(list(row.keys())[:2] + ['best_score'] + list(row.keys())[3:],
                                                  list(row.values())[:2] + [int(list(row.values())[2])] + list(row.values())[3:]))

        data = sorted([func_dict_additem(row) for row in data_
                       if int(row['score']) == max([int(el['score']) for el in data_ if el['email'] == row['email']])
                       and datetime.strptime(row['date_and_time'], "%Y-%m-%d %H:%M:%S") ==
                                             max([datetime.strptime(el1['date_and_time'], "%Y-%m-%d %H:%M:%S")
                                                  for el1 in data_ if el1['email'] == row['email']])
                       ],
                        key=lambda x: x['email'])
        json.dump(data, file2, indent="   ")
        #print(*data, sep='\n')
#exam_result()


def food_services():
    with open("food_services.json", encoding="utf-8") as file:
        data = [row for row in json.load(file)]

        dict_area = {}
        dict_company = {}
        for d in data:
            if d['District'] not in dict_area.keys():
                dict_area[d['District']] = 1
            else:
                dict_area[d['District']] = dict_area.setdefault(d['District']) + 1

            if d['OperatingCompany'] not in dict_company.keys():
                dict_company[d['OperatingCompany']] = 1
            else:
                dict_company[d['OperatingCompany']] = dict_company.setdefault(d['OperatingCompany']) + 1
        print(": ".join(map(str, sorted(dict_area.items(), key=lambda x: x[1], reverse=True)[0])))
        print(": ".join(map(str, sorted(dict_company.items(), key=lambda x: x[1], reverse=True)[1])))
#food_services()


def food_services2():
    with open("food_services (2).json", encoding="utf-8") as file:
        data = json.load(file)

        my_dict = {}
        for d in data:
            if d['TypeObject'] not in my_dict.keys():
                my_dict[d['TypeObject']] = {d['Name']: d['SeatsCount']}
            else:
                if list(my_dict[d['TypeObject']].values())[0] < d['SeatsCount']:
                    my_dict[d['TypeObject']] = {d['Name']: d['SeatsCount']}

        print(*map(lambda x: str(x[0]) + ": " + ", ".join([str(el) for el in list(x[1].items())[0]]),
                        sorted(list(my_dict.items()), key=lambda x: x[0])),
                        sep='\n')

food_services2()