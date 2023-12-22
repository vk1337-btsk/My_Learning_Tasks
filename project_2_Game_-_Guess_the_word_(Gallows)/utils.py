from random import choice


def get_word():
    """Функция выбора случайного слова"""

    # словарь с рабочими словами
    words_list = [
        "Кант", "Хроника", "Зал", "Галера", "Балл", "Вес", "Кафель", "Знак", "Фильтр", "Башня",
        "Кондитер", "Омар", "Чан", "Пламя", "Банк", "Тетерев", "Муж", "Камбала", "Груз", "Кино",
        "Лаваш", "Калач", "Геолог", "Бальзам", "Бревно", "Жердь", "Борец", "Самовар", "Карабин",
        "Подлокотник", "Барак", "Мотор", "Шарж", "Сустав", "Амфитеатр", "Скворечник", "Подлодка",
        "Затычка", "Ресница", "Спичка", "Кабан", "Муфта", "Синоптик", "Характер", "Мафиози",
        "Фундамент", "Бумажник", "Библиофил", "Дрожжи", "Казино", "Конечность", "Пробор", "Дуст",
        "Комбинация", "Мешковина", "Процессор", "Крышка", "Сфинкс", "Пассатижи", "Фунт", "Кружево",
        "Агитатор", "Формуляр", "Прокол", "Абзац", "Караван", "Леденец", "Кашпо", "Баркас", "Кардан",
        "Вращение", "Заливное", "Метрдотель", "Клавиатура", "Радиатор", "Сегмент", "Обещание",
        "Магнитофон", "Кордебалет", "Заварушка"
    ]

    word = choice(words_list).upper()
    return word


def display_hangman(tries):
    """Функция рисования человечка в зависимости от количества ошибок"""
    stages = [

        # финальное состояние: голова, торс, обе руки, обе ноги
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',

        # голова, торс, обе руки, одна нога
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',

        # голова, торс, обе руки
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',

        # голова, торс и одна рука
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',

        # голова и торс
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',

        # голова
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',

        # начальное состояние
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[tries]


def play(word):
    # строка, содержащая символы _ на каждую букву задуманного слова
    word_completion = '_ ' * (len(word) - 1) + '_'
    # список уже названных букв
    guessed_letters = []
    # список уже названных слов
    guessed_words = []
    # количество попыток
    tries = 6
    alphabet = list("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЧЦШЩЪЬЫЭЮЯ")

    print(f"Давайте играть в угадай слова!\n"
          "Попробуйте угадать загаданное слово..."
          f"{display_hangman(tries)}"
          f"{word_completion}\n")

    while True:
        letter = input("Введите букву или слово:\n")

        if not letter:
            # если ничего не ввели (пустая строка)
            print("Вы ничего не ввели. Попробуйте снова...\n")
            continue

        if letter != "":
            # проверка на то, что введены буквы и нет лишнего
            count = 0
            for i in range(len(letter)):
                if list(letter)[i].upper() in alphabet:
                    count += 1
            if count != len(letter):
                print("В написанном вами слове есть недопустимые символы. Попробуйте снова...\n")
                continue

        if len(letter) > len(word):
            # если слово больше загаданного
            print("Введённое вами слово больше загаданного. Попробуйте снова...\n")
            continue

        if 1 < len(letter) < len(word):
            # если слово меньше загаданного
            print("Введённое вами слово меньше загаданного. Попробуйте снова...\n")
            continue

        if letter.upper() in guessed_letters:
            # если уже пробовали эту букву
            print("Вы уже говорили эту букву. Её нет в загаданном слове. Попробуйте ещё разок...\n")
            continue

        if letter.upper() in guessed_words:
            # если уже пробовали эту букву
            print("Вы уже говорили это слово. Это не оно. Попробуйте ещё разок...\n")
            continue

        if (len(letter) == len(word)) and (letter not in guessed_words) and (letter.upper() != word):
            # если не угадали слово

            guessed_words.append(letter.upper())
            tries -= 1
            print(f"Не угадали! Это не загаданное мной слово!\n"
                  f"{display_hangman(tries)}"
                  f"{word_completion}")

        if letter.upper() == word:
            # Если угадали слово полностью
            print("Поздравляю! Вы угадали слово! Это невероятно!\n")
            while True:
                answer = input("Желаете попытать удачу снова? (да или нет):")
                if answer == "да" or answer == "Да":
                    play(get_word())
                elif answer == "нет" or answer == "Нет":
                    print("Тогда до новых встреч!")
                    break
                else:
                    print("Ответьте да или нет")
                    continue
            return

        if (len(letter) == 1) and (letter not in guessed_letters) and (
                letter.upper() not in list(word)):  # если не угадали буквы
            print("Не угадали! Такой буквы нет в загаданном слове.\n")
            guessed_letters.append(letter.upper())
            tries -= 1
            print(display_hangman(tries))
            print(word_completion)

        if letter.upper() in list(word):  # если угадали букву
            print("Поздравляю! Вы угадали, эта буква есть в загаданном слове.\n")
            word_completion = word_completion.split(" ")
            for i in range(len(word)):
                if letter.upper() in list(word)[i]:
                    word_completion[i] = letter.upper()
            word_completion = " ".join(word_completion)
            print(display_hangman(tries))
            print(word_completion)

        if word_completion.split(" ") == list(word):
            # Если угадали слово по буквам
            print('Поздравляем, вы угадали слово! Вы победили!\n')
            while True:
                answer = input("Желаете попытать удачу снова? (да или нет) ")
                if answer == "да" or answer == "Да":
                    play(get_word())
                elif answer == "нет" or answer == "Нет":
                    print("Тогда до новых встреч!")
                    break
                else:
                    print("Ответьте да или нет")
                    continue
            return

        if tries == 0:  # если кончились попытки
            print('Очень жаль... Вы проиграли и не угадали слово.')
            print(display_hangman(tries))
            print('Слово было: ', word)
            while True:
                answer = input("Желаете попытать удачу снова? (да или нет): ")
                if answer == "да" or answer == "Да":
                    play(get_word())
                elif answer == "нет" or answer == "Нет":
                    print("Тогда до новых встреч!")
                    break
                else:
                    print("Ответьте да или нет")
                    continue
            return
