from collections import OrderedDict


def reverse_ordered_dict():
    """
    Вам доступен словарь data. Дополните приведенный ниже код, чтобы он вывел данный словарь, расположив его элементы
    в обратном порядке.
    Примечание. Например, если бы словарь data имел вид:
    data = OrderedDict(key1='value1', key2='value2', key3='value3')
    то программа должна была бы вывести:
    OrderedDict([('key3', 'value3'), ('key2', 'value2'), ('key1', 'value1')])
    """
    my_data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника',
                           'TypeObject': 'кафе', 'AdmArea': 'Центральный административный округ',
                           'District': 'район Арбат', 'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2',
                           'SeatsCount': '10'})
    return OrderedDict(reversed(my_data.items()))
# print(reverse_ordered_dict())


def sorted_ordered_dict():
    """
    Вам доступен словарь data с четным количеством элементов. Дополните приведенный ниже код, чтобы он вывел данный
    словарь, расположив его элементы по следующему правилу: первый, последний, второй, предпоследний, третий, и так
    далее. Примечание. Например, если бы словарь data имел вид:
    data = OrderedDict(key1='value1', key2='value2', key3='value3', key4='value4')
    то программа должны была бы вывести:
    OrderedDict([('key1', 'value1'), ('key4', 'value4'), ('key2', 'value2'), ('key3', 'value3')])
    """
    data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе',
                        'AdmArea': 'Центральный административный округ', 'District': 'район Арбат',
                        'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})
    data_true_false = [not i % 2 == 0 for i in range(len(data))]

    my_data = OrderedDict()

    for d in data_true_false:
        name, grade = data.popitem(last=d)
        my_data[name] = grade
    return my_data
# print(sorted_ordered_dict())


def custom_sort(ordered_dict: OrderedDict, by_values: bool = False) -> None:
    """
    Реализуйте функцию custom_sort(), которая принимает два аргумента в следующем порядке:
    ordered_dict — словарь OrderedDict
    by_values — булево значение, по умолчанию имеет значение False
    Функция должна сортировать словарь ordered_dict:
    по ключам, если by_values имеет значение False
    по значениям, если by_values имеет значение True
    Примечание 1. Функция должна изменять переданный словарь, а не возвращать новый. Возвращаемым значением функции
    должно быть None.
    Примечание 2. Гарантируется, что переданный в функцию словарь можно отсортировать, то есть он не содержит ключи,
    имеющие разные типы, а также значения, имеющие разные типы.
    Примечание 3. Если два элемента имеют равные значения, то следует сохранить их исходный порядок следования.
    """
    sorted_items = sorted(ordered_dict.items(), key=lambda d: d[1 if by_values else 0])
    # Очищаем оригинальный словарь
    ordered_dict.clear()
    # Добавляем отсортированные элементы обратно в оригинальный словарь
    for key, value in sorted_items:
        ordered_dict[key] = value
# data = OrderedDict(Dustin=29, Anabel=17, Brian=40, Carol=16)
# custom_sort(data)
# print(data)
#
# data = OrderedDict(Earth=3, Mercury=1, Mars=4, Venus=2)
# custom_sort(data, by_values=True)
# print(*data.items())