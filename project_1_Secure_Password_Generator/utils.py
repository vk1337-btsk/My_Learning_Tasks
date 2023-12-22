from random import randint, shuffle


def choice_quantity_password():
    """Определяем количество паролей"""
    while True:
        quantity = input("Введите количество паролей для генерации: ")
        if quantity.isdigit():
            return int(quantity)
        else:
            print("Нужно ввести число...")


def choice_length_password():
    """Определяем длину пароля"""
    while True:
        length = input("Введите длину пароля (число): ")
        if length.isdigit():
            return int(length)
        else:
            print("Нужно ввести число...")


def choice_digit_need():
    """Нужны ли цифры?"""
    while True:
        digit_need = input("Нужны ли цифры в пароле? (Да/Нет): ")
        if digit_need.isalpha() and digit_need.lower() in ("да", "нет"):
            return digit_need
        else:
            print("Введите Да или Нет...")


def choice_lower_letters_need():
    """Нужны ли прописные буквы?"""
    while True:
        lower_letters_need = input("Нужны ли прописные буквы в пароле? (Да/Нет) ")
        if lower_letters_need.isalpha() and lower_letters_need.lower() in ("да",  "нет"):
            return lower_letters_need
        else:
            print("Введите Да или Нет...")


def choice_upper_letter_need():
    """Нужны ли прописные буквы?"""
    while True:
        upper_letter_need = input("Нужны ли заглавные буквы в пароле? (Да/Нет) ")
        if upper_letter_need.isalpha() and upper_letter_need.lower() in ("да",  "нет"):
            return upper_letter_need
        else:
            print("Введите Да или Нет...")


def choice_punctuation_need():
    """Нужны ли прописные буквы?"""
    while True:
        punctuation_need = input("Нужны ли специальные символы в пароле? (Да/Нет) ")
        if punctuation_need.isalpha() and punctuation_need.lower() in ("да",  "нет"):
            return punctuation_need
        else:
            print("Введите Да или Нет...")


def choice_ambiguous_symbols_need():
    """Нужно ли исключить неоднозначные символы?"""
    while True:
        ambiguous_symbols_need = input("Нужно ли исключить неоднозначные символы? (Да/Нет) ")
        if ambiguous_symbols_need.isalpha() and ambiguous_symbols_need.lower() in ("да",  "нет"):
            return ambiguous_symbols_need
        else:
            print("Введите Да или Нет...")


def choice_count_symbols(length, digit_need, lower_letters_need, upper_letter_need, punctuation_need):
    """Случайно определяем количество букв (строчных и прописных), а также цифр и спец. символов в пароле"""
    while True:
        if digit_need:
            count_digit = randint(1, length)
        else:
            count_digit = 0
        if lower_letters_need:
            count_lower_letters = randint(1, length)
        else:
            count_lower_letters = 0
        if upper_letter_need:
            count_upper_letter = randint(1, length)
        else:
            count_upper_letter = 0
        if punctuation_need:
            count_punctuation = randint(1, length)
        else:
            count_punctuation = 0
        if count_digit + count_lower_letters + count_upper_letter + count_punctuation == length:
            break
        else:
            continue
    return count_digit, count_lower_letters, count_upper_letter, count_punctuation


def delete_ambiguous_symbols(ambiguous_symbols, digits, lower_case_letters, upper_case_letters, punctuation):
    """Удаляем неоднозначные символы"""
    for i in range(len(ambiguous_symbols)):
        while ambiguous_symbols[i] in digits:
            digits.remove(ambiguous_symbols[i])
        while ambiguous_symbols[i] in lower_case_letters:
            lower_case_letters.remove(ambiguous_symbols[i])
        while ambiguous_symbols[i] in upper_case_letters:
            upper_case_letters.remove(ambiguous_symbols[i])
        while ambiguous_symbols[i] in punctuation:
            punctuation.remove(ambiguous_symbols[i])
    return digits, lower_case_letters, upper_case_letters, punctuation


def create_password(digits, lowercase_letters, uppercase_letters, punctuation, count_digit, count_lower_letters,
                    count_upper_letter, count_punctuation):
    password = []
    if count_digit > 0:
        for i in range(count_digit):
            password.append(digits[randint(0, len(digits)-1)])
    if count_lower_letters > 0:
        for i in range(count_lower_letters):
            password.append(lowercase_letters[randint(0, len(lowercase_letters) - 1)])
    if count_upper_letter > 0:
        for i in range(count_upper_letter):
            password.append(uppercase_letters[randint(0, len(uppercase_letters) - 1)])
    if count_punctuation > 0:
        for i in range(count_punctuation):
            password.append(punctuation[randint(0, len(punctuation) - 1)])
    shuffle(password)
    password = "".join(password)
    return password
