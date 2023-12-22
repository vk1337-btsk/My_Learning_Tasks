data = list()
symbols = list(" !@#$%^&*()+-*/,.?\"\'")
data_eng = list("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz")
data_rus = list("абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя")


def choice_encrypt_or_decrypt_and_language():
    # target: 1-шифр, 2-дешифр; language: 1-англ, 2-рус
    while True:
        target = input("Желаете зашифровать или дешифровать текст? (1 - зашифровать, 2 - дешифровать): ")
        if not target.isdigit():
            print("Напишите 1 или 2...")
            continue
        target = int(target)
        if target == 1 or target == 2:
            break
        else:
            print("Напишите 1 или 2...")
            continue

    while True:
        language = input("Текст будет на английском или русском? (1 - английский, 2 - русский): ")
        if not language.isdigit():
            print("Напишите 1 или 2...")
            continue
        language = int(language)
        if language == 1:
            data = data_eng
            break
        elif language == 2:
            data = data_rus
            break
        else:
            print("Напишите 1 или 2...")
            continue

    return target, language, data


def enter_and_check_text_to_encrypt_or_decrypt(target, language, date, symbols):
    if target == 1:
        targ1, targ = "шифрованию", "зашифровать"
    else:
        targ1, targ = "дешифрованию", "дешифровать"
    if language == 1:
        lang = "английском"
    else:
        lang = "русском"
    question = "Введите текст на {} который нужно {}: ".format(lang, targ)
    count = 0
    while True:
        s = input(question)
        for i in range(len(s)):
            if (s[i]).lower() in date or s[i] in symbols:   count += 1
        if count == len(s):
            print("Введён корректный текст. Приступаем к {}...".format(targ1))
            break
        else:
            print("Введён некорректный текст. Введите корректный текст...")
            continue
    return s


def encrypt_text(s, date):
    s1 = list(s)
    cipher = []

    while True:
        keys = input("Введите ключ (значение сдвига), введите число не равное нулю: ")
        if keys.isdigit() == True or keys[1:].isdigit() == True:
            print("Введённый ключ корректен.")
            break
        else:
            print("Введите ключ (число не равное нулю) - значение сдвига текста")
            continue
    keys = int(keys)

    while keys > len(date) / 2:
        keys -= int(len(date) / 2)
    while keys < -len(date) / 2:
        keys += int(len(date) / 2)

    if keys == 0:
        print(
            "Вы ввели ключ, равный нулю или кратный самому себе, тем самым текст не изменился. Попробуйте ввести ключ ещё раз")
        encrypt_text(s, date)

    if keys > 0:
        for i in range(len(s)):
            if (s1[i]).lower() == s1[i] and (s1[i]).lower() in date:
                cipher.append(date[date.index((s1[i]).lower()) + keys])
            elif (s1[i]).lower() != s1[i] and (s1[i]).lower() in date:
                cipher.append(date[date.index((s1[i]).lower()) + keys].upper())
            elif s[i] in symbols:
                cipher.append(s[i])

    if keys < 0:
        date_reverse = date[::-1]
        for i in range(len(s)):
            if (s1[i]).lower() == s1[i] and (s1[i]).lower() in date_reverse:
                cipher.append(date_reverse[date_reverse.index((s1[i]).lower()) - keys])
            elif (s1[i]).lower() != s1[i] and (s1[i]).lower() in date_reverse:
                cipher.append(date_reverse[date_reverse.index((s1[i]).lower()) - keys].upper())
            elif s[i] in symbols:
                cipher.append(s[i])

    cipher = "".join(cipher)
    return cipher


def decrypt_text(s, date):
    s1 = list(s)
    cipher = []

    while True:
        keys1 = input("Введите максимальное значение ключа (значение сдвига), введите число не равное нулю: ")
        if keys1.isdigit() == True or keys1[1:].isdigit() == True:
            print("Введённый ключ корректен.")
            break
        else:
            print("Введите ключ (число не равное нулю) - значение сдвига текста")
            continue
    keys1 = int(keys1)

    while keys1 > len(date) / 2:
        keys1 -= int(len(date) / 2)
    while keys1 < -len(date) / 2:
        keys1 += int(len(date) / 2)

    if keys1 < 0:
        cipher_options = []
        for keys in range(0, keys1 - 1, -1):
            cipher = []
            for i in range(len(s)):
                if (s1[i]).lower() == s1[i] and (s1[i]).lower() in date:
                    cipher.append(date[date.index((s1[i]).lower()) - keys])
                elif (s1[i]).lower() != s1[i] and (s1[i]).lower() in date:
                    cipher.append(date[date.index((s1[i]).lower()) - keys].upper())
                elif s[i] in symbols:
                    cipher.append(s[i])
            cipher = "".join(cipher)
            cipher_options.append(cipher)

    if keys1 > 0:
        cipher_options = []
        for keys in range(1, keys1 + 1):
            cipher = []
            date_reverse = date[::-1]
            for i in range(len(s)):
                if (s1[i]).lower() == s1[i] and (s1[i]).lower() in date_reverse:
                    cipher.append(date_reverse[date_reverse.index((s1[i]).lower()) - keys])
                elif (s1[i]).lower() != s1[i] and (s1[i]).lower() in date_reverse:
                    cipher.append(date_reverse[date_reverse.index((s1[i]).lower()) - keys].upper())
                elif s[i] in symbols:
                    cipher.append(s[i])
            cipher = "".join(cipher)
            cipher_options.append(cipher)

    return cipher_options