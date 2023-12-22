from utils import *

date = list()
symbols = list(" !@#$%^&*()+-*/,.?\"\'")
date_eng = list("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz")
date_rus = list("абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя")


if __name__ == "__main__":
    print("Добро пожаловать в программу шифрования/дешифрования текста по методу шифра Цезаря.")

    target, language, date = choice_encrypt_or_decrypt_and_language()

    s = enter_and_check_text_to_encrypt_or_decrypt(target, language, date, symbols)

    if target == 1:
        print('Ваш текст "{}" после шифрования стал текстом "{}".'.format(s, encrypt_text(s, date)))
    else:
        cipher_options = decrypt_text(s, date)
        print('\nВарианты расшифровки вашего текста "{}":'.format(s))
        print(*cipher_options, sep="\n")