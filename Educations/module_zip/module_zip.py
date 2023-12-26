from zipfile import ZipFile
from datetime import datetime
import os.path
import json


def count_files_in_zip():
    with ZipFile("workbook.zip") as zip_file:
        count_file = sum([int(not file.is_dir()) for file in zip_file.infolist()])
        return print(count_file)
#count_files_in_zip()


def print_size_zip_before_and_after():
    with ZipFile("workbook.zip") as zip_file:
        sourse_size = 0
        compressed_size = 0
        for file in zip_file.infolist():
            sourse_size += file.file_size
            compressed_size += file.compress_size

        return print(f"""\
Объем исходных файлов: {sourse_size} байт(а)
Объем сжатых файлов: {compressed_size} байт(а)""")
#print_size_zip_before_and_after()


def best_compression_ratio():
    with ZipFile('workbook.zip') as zip_file:
        my_dict = {file.filename[file.filename.find("/")+1:]: round((file.compress_size/file.file_size)*100, 2)
                   for file in zip_file.infolist() if file.compress_size != 0 and file.file_size != 0}
        return print(min(my_dict.items(), key=lambda x: x[1])[0])
#best_compression_ratio()


def select_favorites_files():
    with ZipFile("workbook.zip") as zip_file:
        my_list = [file.filename[file.filename.find("/")+1:] for file in zip_file.infolist()
                   if not file.is_dir() and
                   datetime(*file.date_time) > datetime(2021, 11, 30, 14, 22, 0)]
        return print(*sorted(my_list), sep='\n')
#select_favorites_files()


def formatted_output():
    with ZipFile('workbook.zip') as zip_file:
        print_info = lambda f: f"""\r{f.filename[f.filename.find("/")+1:]}
                    \r  Дата модификации файла: {datetime.strftime(datetime(*f.date_time), '%Y-%m-%d %H:%M:%S')}
                    \r  Объем исходного файла: {f.file_size} байт(а)
                    \r  Объем сжатого файла: {f.compress_size} байт(а)"""

        my_list = [print_info(file) for file in sorted(zip_file.infolist(),
                                                       key=lambda x: x.filename[x.filename.find("/")+1:])
                                                       if not file.is_dir()]
        return print(*my_list, sep="\n\n", end='')
#formatted_output()


def write_files_in_zip():
    file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
                  'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
                  'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py']

    with ZipFile('files.zip', mode='w') as zip_file:
        for file in file_names:
            zip_file.write(file)
#write_files_in_zip()


def add_file_in_zip_if_size_less_100():
    file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
                  'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
                  'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py']

    with ZipFile('files.zip', mode='a') as zip_file:
        for file in file_names:
            if os.path.getsize(file) < 100:
                zip_file.write(file)
#add_file_in_zip_if_size_less_100()


def extract_this(zip_name, *args):
    with ZipFile(zip_name) as zip_file:
        if args:
            info = zip_file.infolist()
            for arg in args:
                for file in info:
                    if arg in file.filename:
                        zip_file.extract(file)
                        break
        else:
            zip_file.extractall()
#extract_this('workbook.zip', 'earth.jpg', 'exam.txt')


def select_and_process_json():
    # Открываем zip и получаем список файлов
    with ZipFile('data.zip') as zip_file:
        info = zip_file.infolist()

        # Выводим названия файлов в кодировке UTF-8
        filenames = [f.filename.encode('cp437', errors='replace').decode('cp866', errors='replace')
                     for f in info]
        #print(*filenames, sep='\n')

        names = []
        # Проходим по файлам в списке файлов
        for file in info:
            if file.filename.endswith(".json"):
                with zip_file.open(file.filename) as json_file:
                    try:
                        json_data = json.load(json_file)
                        #print(json_data)
                        if json_data['team'] == 'Arsenal':
                            names.append([json_data['first_name'], json_data['last_name']])
                    except:
                        pass
        print(*map(lambda x: " ".join(x), sorted(sorted(names, key=lambda n: n[1]), key=lambda n: n[0])), sep='\n')
#select_and_process_json()


def print_archive_structure():
    with ZipFile('desktop.zip') as zip_file:
        info = zip_file.infolist()

        func_cup_end = lambda x: x[:-1] if x.endswith('/') else x

        func_space = lambda x: "  " * func_cup_end(x).count('/') + func_cup_end(x)[func_cup_end(x).rfind('/') + 1:]

        func_is_dir = lambda x: "" if file.is_dir() else func_size(file)
        func_size = lambda x: (f' {int(round(x.file_size, 0))} B' if len(str(x.file_size)) <= 3 else
                               f' {int(round(x.file_size / 1024, 0))} KB' if 4 < len(str(x.file_size)) <= 6 else
                               f' {int(round(x.file_size / 1024 / 1024, 0))} MB' if 6 < len(str(x.file_size)) <= 9 else
                               f' {int(round(x.file_size / 1024 / 1024 / 1024, 0))} GB')

        for file in info:
            print(f"{func_space(file.filename)}{func_is_dir(file)}")
#print_archive_structure()