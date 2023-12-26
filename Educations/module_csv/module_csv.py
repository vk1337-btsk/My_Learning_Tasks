import csv
from datetime import datetime


def task_discount(variant):
    """Скидки
    Наступил ноябрь, и во многих магазинах начались распродажи, но как многим известно, зачастую товары со скидкой
    оказываются дороже, чем без нее. Вам доступен файл sales.csv, который содержит данные о ценообразовании различной
     бытовой техники. В первом столбце записано название товара, во втором — старая цена, в третьем — новая цена со
     скидкой:

    name;old_price;new_price
    Встраиваемая посудомоечная машина De'Longhi DDW 06S;23089;31862
    Вытяжка Falmec Afrodite 60/600;27694;18001
    ...
    Напишите программу, которая выводит названия тех товаров, цена на которые уменьшилась. Товары должны быть
    расположены в своем исходном порядке, каждый на отдельной строке.

    Примечание 1. Разделителем в файле sales.csv является точка с запятой, при этом кавычки не используются.

    Примечание 2. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.

    Примечание 3. Начальная часть ответа выглядит так:

    Вытяжка Falmec Afrodite 60/600
    Духовой шкаф AEG BS 5836600
    Вытяжка MAUNFELD PLYM 60
    ...
    Примечание 4. При открытии файла используйте явное указание кодировки UTF-8."""

    with open("sales.csv", encoding="utf-8") as file:

        # Читаем просто через read как текст, не используя модуль csv
        if variant == 1:
            data = file.read()
            my_data = []
            for line in data.splitlines()[1:]:
                name, old_price, new_price = str(line.split(";")[0]), int(line.split(";")[1]), int(line.split(";")[2])
                if old_price > new_price:
                    print(name)
                    my_data.append(name)

        # Читаем через объект reader
        elif variant == 2:
            data_ = [row for row in csv.reader(file, delimiter=";")]
            data = [[str(el[0]), int(el[1]), int(el[2])] for el in data_[1:]]
            my_data = []
            for d in data:
                if d[1] > d[2]:
                    print(d[0])
                    my_data.append(d[0])

        # Читаем через объект DictReader
        elif variant == 3:
            data_ = csv.DictReader(file, delimiter=";")
            my_data = []
            for d in data_:
                if int(d['old_price']) > int(d['new_price']):
                    print(d['name'])
                    my_data.append(d['name'])

    # Записываем просто через file.write в .txt
    with open("clue_sales_my_answers.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(my_data))
# task_discount(3)


def task_average_sales():
    """
    Вам доступен файл salary_data.csv, который содержит анонимную информацию о зарплатах сотрудников в различных
    компаниях. В первом столбце записано название компании, а во втором — зарплата очередного сотрудника:

    company_name;salary
    Atos;135000
    ХайТэк;24400
    Philax;128600
    Инлайн Груп;43900
    IBS;70600
    Oracle;131600
    Atos;91000
    ...
    Напишите программу, которая упорядочивает компании по возрастанию средней зарплаты ее сотрудников и выводит их
    названия, каждое на отдельной строке. Если две компании имеют одинаковые средние зарплаты, они должны быть
    расположены в лексикографическом порядке их названий.

    Примечание 1. Средняя зарплата компании определяется как отношение суммы всех зарплат к их количеству.

    Примечание 2. Разделителем в файле salary_data.csv является точка с запятой, при этом кавычки не используются.

    Примечание 3. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.

    Примечание 4. Начальная часть ответа выглядит так:

    Информзащита
    Форс
    OFT group
    ...
    Примечание 5. При открытии файла используйте явное указание кодировки UTF-8.
    """
    with open("salary_data.csv", encoding="utf-8") as file:
        data = csv.DictReader(file, delimiter=";")
        my_dict = {}

        for d in data:
            if d['company_name'] not in my_dict.keys():
                my_dict[d['company_name']] = {"sales": [int(d['salary'])], "average_sale": 0}
            else:
                my_dict[d['company_name']]["sales"].append(int(d['salary']))
            my_dict[d['company_name']]["average_sale"] = sum(my_dict[d['company_name']]["sales"]) / len(
                my_dict[d['company_name']]["sales"])
        print(*dict(sorted(my_dict.items(), key=lambda x: x[1]['average_sale'])).keys(), sep="\n")
# task_average_sales()


def task_sorted_in_column(column):
    """
    Вам доступен файл deniro.csv, каждый столбец которого содержит либо только числа, либо строковые значения:

    Machete,2010,72
    Marvin's Room,1996,80
    Raging Bull,1980,97
    ...
    Напишите программу, которая сортирует содержимое данного файла по указанному столбцу. Причем данные должны быть
    отсортированы в порядке возрастания чисел, если столбец содержит числа, и в лексикографическом порядке слов, если
    столбец содержит слова.

    Формат входных данных
    На вход программе подается натуральное число — номер столбца файла deniro.csv.

    Формат выходных данных
    Программа должна отсортировать содержимое файла deniro.csv по введенному столбцу и вывести полученный результат
    в исходном формате.

    Примечание 1. Нумерация столбцов начинается с единицы.

    Примечание 2. Например, если бы файл deniro.csv имел вид:

    red,4
    blue,3
    green,28
    purple,1
    и его требовалось отсортировать по второму столбцу (в порядке возрастания чисел), то программа должна была бы
    вывести:

    purple,1
    blue,3
    red,4
    green,28
    Примечание 3. Если две какие-либо строки имеют одинаковые значения в столбцах, то следует сохранить их исходный
    порядок следования.

    Примечание 4. Разделителем в файле deniro.csv является запятая, при этом кавычки не используются.

    Примечание 5. Указанный файл доступен по ссылке. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub
    Примечание 6. При открытии файла используйте явное указание кодировки UTF-8.
    """
    with open("deniro.csv", encoding="utf-8") as file:
        data = csv.reader(file, delimiter=",")
        my_data = [[str(row[0]), int(row[1]), int(row[2])] for row in data]
        print(*list(map(lambda d: ",".join([str(el) for el in d]), sorted(my_data, key=lambda x: x[column - 1]))),
              sep="\n")
# task_sorted_in_column(1)


def task_csv_columns(filename):
    """
    Реализуйте функцию csv_columns(), которая принимает один аргумент:

    filename — название csv файла, например, data.csv
    Функция должна возвращать словарь, в котором ключом является название столбца файла filename, а значением — список
    элементов этого столбца.

    Примечание 1. Гарантируется, что в передаваемом в функцию файле разделителем является запятая, при этом кавычки не
    используются.

    Примечание 2. Гарантируется, что у передаваемого в функцию файла первая строка содержит названия столбцов.

    Примечание 3. Например, если бы файл exam.csv имел вид:

    name,grade
    Timur,5
    Arthur,4
    Anri,5
    то следующий вызов функции csv_columns():

    csv_columns('exam.csv')
    должен был бы вернуть:

    {'name': ['Timur', 'Arthur', 'Anri'], 'grade': ['5', '4', '5']}
    Примечание 4. Ключи в словаре, а также элементы в списках должны располагаться в своем исходном порядке.
    """
    with open(filename, encoding="utf-8") as file:
        data = csv.reader(file, delimiter=",")
        my_data = [row for row in data]
        my_dict = {}
        for number, d in enumerate(my_data[0]):
            my_dict[d] = []
            for n in my_data[1:]:
                my_dict[d].append(n[number])
    return my_dict
# print(task_csv_columns('deniro2.csv'))


def task_popular_domain():
    """
    Вам доступен файл data.csv, который содержит неповторяющиеся данные о пользователях некоторого ресурса. В первом
    столбце записано имя пользователя, во втором — фамилия, в третьем — адрес электронной почты:

    first_name,surname,email
    John,Wilson,johnwilson@outlook.com
    Mary,Wilson,marywilson@list.ru
    ...
    Напишите программу, которая создает файл domain_usage.csv, имеющий следующее содержание:

    domain,count
    rambler.ru,24
    iCloud.com,29
    ...
    где в первом столбце записано название почтового домена, а во втором — количество пользователей, использующих
    данный домен. Домены в файле должны быть расположены в порядке возрастания количества их использований, при
    совпадении количества использований — в лексикографическом порядке.

    Примечание 1. Разделителем в файле data.csv является запятая, при этом кавычки не используются.

    Примечание 2. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.

    Примечание 3. Начальная часть файла domain_usage.csv выглядит так:

    domain,count
    rambler.ru,24
    iCloud.com,29
    ...
    Примечание 4. При открытии файла используйте явное указание кодировки UTF-8.
    """
    with open("data.csv", encoding="utf-8") as file:
        data = csv.DictReader(file, delimiter=",")
        data = [row for row in data]
        my_dict = {}
        for d in data:
            domain = d["email"][d["email"].index("@") + 1:]
            if domain not in my_dict.keys():
                my_dict[domain] = 1
            else:
                my_dict[domain] = my_dict.setdefault(domain) + 1
        my_data = sorted(sorted(list(my_dict.items()), key=lambda x: x[0]), key=lambda x: x[1])
    with open("domain_usage.csv", "w", encoding="utf-8", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["domain", "count"])
        for row in my_data:
            writer.writerow(row)
        print(my_data)
    return
# task_popular_domain()


def task_wifi_in_moscow():
    """
    Вам доступен файл wifi.csv, который содержит данные о городском Wi-Fi Москвы. В первом столбце записано название
    округа, во втором — название района, в третьем — адрес, в четвертом — количество точек доступа по этому адресу:

    adm_area;district;location;number_of_access_points
    Центральный административный округ;район Якиманка;город Москва, улица Серафимовича, дом 5/16;5
    Центральный административный округ;район Якиманка;город Москва, Болотная набережная, дом 11, строение 1;2
    ...
    Напишите программу, которая определяет количество точек доступа в каждом районе Москвы и выводит названия всех
    районов, для каждого указывая соответствующее количество точек доступа, каждое на отдельной строке, в следующем
    формате:

    <название района>: <количество точек доступа>
    Названия районов должны быть расположены в порядке убывания количества точек доступа, при совпадении количества
    точек доступа — в лексикографическом порядке.

    Примечание 1. Разделителем в файле wifi.csv является точка с запятой, при этом кавычки не используются.

    Примечание 2. При сортировке названия районов должны быть использованы именно в том виде, в котором они указаны в
    исходном файле. Выполнять какие-либо дополнительные преобразования не нужно.

    Примечание 3. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.

    Примечание 4. Начальная часть ответа выглядит так:

    Тверской район: 480
    район Хамовники: 386
    Пресненский район: 349
    ...
    Примечание 5. При открытии файла используйте явное указание кодировки UTF-8.
    """
    with open("wifi.csv", encoding="utf-8") as file:
        data = csv.DictReader(file, delimiter=";")
        my_data = [row for row in data]
        my_dict = {}
        for d in my_data:
            if d["district"] not in my_dict.keys():
                my_dict[d['district']] = int(d['number_of_access_points'])
            else:
                my_dict[d['district']] = my_dict.setdefault(d['district']) + int(d['number_of_access_points'])
    return print(*list(map(lambda x: ": ".join(map(str, x)), sorted(my_dict.items(), key=lambda x: (-x[1], x[0])))),
                 sep="\n")
# task_wifi_in_moscow()


def task_last_day_on_titanic():
    """
    Вам доступен файл titanic.csv, который содержит данные о пассажирах, присутствовавших на борту парохода Титаник.
    В первом столбце указана единица, если пассажир выжил, и ноль в противном случае, во втором столбце записано полное
    имя пассажира, в третьем — пол, в четвертом — возраст:

    survived;name;sex;age
    0;Mr. Owen Harris Braund;male;22
    1;Mrs. John Bradley (Florence Briggs Thayer) Cumings;female;38
    ...
    Напишите программу, которая выводит имена выживших пассажиров, которым было менее 18 лет, каждое на отдельной
    строке. Причем сначала должны быть расположены имена всех пассажиров мужского пола, а затем — женского, имена же
    непосредственно в мужском и женском списках должны быть расположены в своем исходном порядке.

    Примечание 1. Разделителем в файле titanic.csv является точка с запятой, при этом кавычки не используются.

    Примечание 2. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.

    Примечание 3. Часть ответа выглядит так:

    Master. Gerios Moubarek
    Master. Alden Gates Caldwell
    ...
    Master. Harold Theodor Johnson
    Mrs. Nicholas (Adele Achem) Nasser
    Miss. Marguerite Rut Sandstrom
    ...
    Примечание 4. При открытии файла используйте явное указание кодировки UTF-8.
    """
    with open("titanic.csv", encoding="utf-8") as file:
        data = csv.DictReader(file, delimiter=";")
        my_data = [row for row in data]
        my_data = list(filter(lambda x: int(x['survived']) == 1 and float(x['age']) < float(18), my_data))
        my_data = sorted(my_data, key=lambda x: x['sex'], reverse=True)
        print(*list(map(lambda x: str(x['name']), my_data)), sep='\n')
        """
        print(*list(map(lambda x: str(x['name']),
              sorted(list(filter(lambda x: int(x['survived']) == 1 and float(x['age']) < float(18),
              [row for row in csv.DictReader(file, delimiter=";")])), key=lambda x: x['sex'], reverse=True))), sep='\n')        
        """
    return
# task_last_day_on_titanic()


def task_log_file():
    """
    Вам доступен файл name_log.csv, в котором находятся логи изменения имени пользователя. В первом столбце записано
    измененное имя пользователя, во втором — адрес электронной почты, в третьем — дата и время изменения. При этом
    email пользователь менять не может, только имя:

    username,email,dtime
    rare_charles6,charlesthompson@inbox.ru,15/11/2021 08:15
    busy_patricia5,patriciasmith@bk.ru,07/11/2021 08:07
    ...
    Напишите программу, которая отбирает из файла name_log.csv только самые свежие записи для каждого пользователя и
    записывает их в файл new_name_log.csv. В файле new_name_log.csv первой строкой должны быть заголовки столбцов
    такие же, как в файле name_log.csv. Логи в итоговом файле должны быть расположены в лексикографическом порядке
    названий электронных ящиков пользователей.

    Примечание 1. Для части пользователей в исходном файле запись только одна, и тогда в итоговый файл следует записать
    только ее, для некоторых пользователей есть несколько записей с разными именами.

    Например, пользователь с электронной почтой c3po@gmail.com несколько раз менял имя:

    C=3PO,c3po@gmail.com,16/11/2021 17:10
    C3PO,c3po@gmail.com,16/11/2021 17:15
    C-3PO,c3po@gmail.com,16/11/2021 17:24
    Из этих трех записей в итоговый файл должна быть записана только одна — самая свежая:

    C-3PO,c3po@gmail.com,16/11/2021 17:24
    Примечание 2. Разделителем в файле name_log.csv является запятая, при этом кавычки не используются.

    Примечание 3. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.

    Примечание 4. Начальная часть файла new_name_log.csv выглядит так:

    username,email,dtime
    angry-barbara2,barbaraanderson@bk.ru,17/11/2021 01:17
    dead-barbara6,barbarabrown@rambler.ru,27/11/2021 08:27
    busy_barbara7,barbaradavis@aol.com,24/11/2021 08:24
    ...
    Примечание 5. При открытии файла используйте явное указание кодировки UTF-8.
    """
    with open("name_log.csv", encoding="utf-8") as file:
        data = csv.DictReader(file, delimiter=",")
        my_data = [row for row in data]
        columns = list(my_data[0].keys())
        my_dict = {d['email']: d for d in sorted(my_data, key=lambda x:
        (datetime.strptime(x['dtime'], "%d/%m/%Y %H:%M"), x['email']))}
        my_dict = {key: my_dict[key] for key in sorted(my_dict.keys())}
    with open("new_name_log.csv", "w", encoding="utf-8", newline="") as file:
        data = my_dict.values()
        writer = csv.DictWriter(file, fieldnames=columns, delimiter=",")
        writer.writeheader()
        for row in data:
            writer.writerow(row)
    return
# task_log_file()


def task_condense_csv(filename, id_name):
    """Рассмотрим следующий текстовый фрагмент:

    ball,color,purple
    ball,size,4
    ball,notes,it's round
    cup,color,blue
    cup,size,1
    cup,notes,none
    Каждая строка этого фрагмента содержит три значения через запятую: имя объекта, свойство этого объекта, значение
    свойства. Например, в первой строке указан объект ball, имеющий свойство color, значение которого равно purple.
    Также у объекта ball есть свойства size и notes, имеющие значения 4 и it's round соответственно. Помимо объекта
    ball имеется объект cup, имеющий те же свойства и в том же количестве. Дадим этим объектам общее название object
    и сгруппируем строки данного текстового фрагмента по первому столбцу:

    object,color,size,notes
    ball,purple,4,it's round
    cup,blue,1,none
    Мы получили запись в привычном CSV формате, в котором в первом столбце указывается имя объекта, а в последующих —
    значения соответствующих свойств этого объекта.

    Реализуйте функцию condense_csv(), которая принимает два аргумента в следующем формате:

    filename — название csv файла, например, data.csv; формат содержимого файла аналогичен формату текстового фрагмента,
    рассмотренного в условии задачи: каждая строка файла содержит три значения через запятую, а именно имя объекта,
    свойство этого объекта, значение свойства; все объекты имеют равные свойства и в равных количествах
    id_name —  общее название для объектов.
    Функция должна привести содержимое файла в привычный CSV формат, сгруппировав строки по первому столбцу и назвав
    первый столбец id_name. Полученный результат функция должна записать в файл condensed.csv.
    Примечание 1. Например, если бы файл data.csv имел следующий вид:

    01,Title,Ran So Hard the Sun Went Down
    02,Title,Honky Tonk Heroes (Like Me)
    то вызов функции condense_csv():

    condense_csv('data.csv', id_name='ID')
    должен был бы создать файл condensed.csv со следующим содержанием:

    ID,Title
    01,Ran So Hard the Sun Went Down
    02,Honky Tonk Heroes (Like Me)
    Примечание 2. Гарантируется, что в передаваемом в функцию csv файле разделителем является запятая, при этом кавычки
    не используются.

    Примечание 3. При открытии файла используйте явное указание кодировки UTF-8.

    Примечание 4. В тестирующую систему сдайте программу, содержащую только необходимую функцию condense_csv(),
    но не код, вызывающий ее.
    """

    with open(filename, encoding="utf-8") as file:
        data = csv.reader(file, delimiter=",")
        data = [row for row in data]
    names = [id_name]
    for n in data:
        if n[1] not in names:
            names.append(n[1])
    my_dict = {}
    for d in data:
        if d[0] not in my_dict:
            my_dict[d[0]] = {}
            my_dict[d[0]].setdefault(id_name, d[0])
            my_dict[d[0]].setdefault(d[1], d[2])
        else:
            my_dict[d[0]].setdefault(d[1], d[2])
    with open("condensed.csv", "w", encoding="utf-8", newline="") as file:
        data = list(my_dict.values())
        writer = csv.DictWriter(file, fieldnames=names, delimiter=",")
        writer.writeheader()
        for row in data:
            writer.writerow(row)
    return
# task_condense_csv('data.csv', id_name='Position')


def task_students():
    """
    Вам доступен файл student_counts.csv, который содержит данные о количестве учеников в некотором учебном заведении
    за период 2000 — 2021 г. В первом столбце записан год, в последующих столбцах записан класс и количество учеников
    в данном классе в этом году:

    year,5-Б,3-Б,8-А,2-Г,7-Б,1-Б,3-Г,3-А,2-В,6-Б,6-А,8-Б,8-Г,11-А,2-А,7-А,5-А,2-Б,10-А,11-Б,8-В,4-А,7-В,3-В,1-А,9-А,11-В
    2000,19,15,18,29,19,17,26,29,28,30,26,27,27,22,29,19,27,20,16,18,15,27,19,29,22,20,23
    2001,21,30,22,19,26,20,24,27,20,30,24,30,29,21,20,19,29,27,23,25,30,30,23,22,22,18,22
    ...
    Напишите программу, которая записывает данную таблицу в файл sorted_student_counts.csv, располагая все столбцы
    в порядке возрастания классов, при совпадении классов — в порядке возрастания букв.

    Примечание 1. Каждый класс содержит номер и букву и записывается в следующем формате:

    <номер класса>-<буква класса>
    Примечание 2. Разделителем в файле student_counts.csv является запятая, при этом кавычки не используются.

    Примечание 3. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.

    Примечание 4. Начальная часть файла sorted_student_counts.csv выглядит так:

    year,1-А,1-Б,2-А,2-Б,...
    2000,22,17,29,20,...
    2001,22,20,20,27,...
    ...
    Примечание 5. При открытии файла используйте явное указание кодировки UTF-8.
    """
    with open("student_counts.csv", encoding="utf-8") as file:
        data = csv.DictReader(file, delimiter=",")
        my_data = [row for row in data]
        names = list(my_data[0].keys())
        names = names[:1] + sorted(names[1:], key=lambda x: (int(x.split("-")[0]), str(x.split("-")[1])))

    with open("sorted_student_counts.csv", "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=names, delimiter=",")
        writer.writeheader()
        for row in my_data:
            writer.writerow(row)
    return
# task_students()


def task_prices():
    """
    Дима очень хочет поесть, но денег у него мало. Помогите ему определить самый дешевый продукт, а также магазин,
    в котором он продается. Вам доступен файл prices.csv, который содержит информацию о ценах продуктов в различных
    магазинах. В первом столбце записано название магазина, а в последующих — цена на соответствующий товар в этом
    магазине:

    Магазин;Творог;Гречка;Рис;Бородинский хлеб;Яблоки;Пельмени;Овсяное печенье;Спагетти;Печеная фасоль;Мороженое;Фарш;
    Вареники;Картофель;Батончик
    Пятерочка;69;133;129;83;141;90;72;123;149;89;88;106;54;84
    Магнит;102;87;95;75;109;112;97;82;101;134;69;61;141;79
    ...
    Напишите программу, которая определяет и выводит самый дешевый продукт и название магазина, в котором он продается,
    в следующем формате:

    <название продукта>: <название магазина>
    Если имеется несколько самых дешевых товаров, то следует вывести тот товар, чье название меньше в
     лексикографическом сравнении. Если один товар продается в нескольких магазинах по одной минимальной цене,
      то следует вывести тот магазин, чье название меньше в лексикографическом сравнении.

    Примечание 1. Разделителем в файле prices.csv является точка с запятой, при этом кавычки не используются.

    Примечание 2. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.

    Примечание 3. Пример вывода:

    Клубничный йогурт: ВкусВилл
    Примечание 4. При открытии файла используйте явное указание кодировки UTF-8.
"""
    with open("prices.csv", encoding="utf-8") as file:
        data = [row for row in csv.DictReader(file, delimiter=";")]
        min_prices = min([min([int(el) for el in list(d.values())[1:]]) for d in data[1:]])
        my_dict = {}
        for d in data:
            for key, value in d.items():
                if value.isdigit() and int(value) == min_prices:
                    my_dict.setdefault(d["Магазин"], key)
        print(": ".join(sorted(my_dict.items(), key=lambda x: (x[1], x[0]))[0][::-1]))
    return
#task_prices()
