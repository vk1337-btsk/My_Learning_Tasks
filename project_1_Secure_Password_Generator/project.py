from utils import *

digits = list("0123456789")
lowercase_letters = list("abcdefghijklmnopqrstuvwxyz")
uppercase_letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
punctuation = list("!#$%&*+-=?@^_")
ambiguous_symbols = list("il1Lo0O")


if __name__ == "__main__":
    # Определяем атрибуты пароля
    quantity = choice_quantity_password()
    length = choice_length_password()
    digit_need = choice_digit_need()
    lower_letters_need = choice_lower_letters_need()
    upper_letter_need = choice_upper_letter_need()
    punctuation_need = choice_punctuation_need()
    ambiguous_symbols_need = choice_ambiguous_symbols_need()

    # Определяем количество символов
    count_digit, count_lower_letters, count_upper_letter, count_punctuation = (
        choice_count_symbols(length, digit_need, lower_letters_need, upper_letter_need, punctuation_need))

    # Удаляем неоднозначные символы (при необходимости)
    if ambiguous_symbols_need:
        digits, lowercase_letters, uppercase_letters, punctuation = (
            delete_ambiguous_symbols(ambiguous_symbols, digits, lowercase_letters, uppercase_letters, punctuation))

    # Создаём список с паролями
    passwords = []
    for i in range(quantity):
        password = create_password(digits, lowercase_letters, uppercase_letters, punctuation, count_digit,
                                   count_lower_letters, count_upper_letter, count_punctuation)
        passwords.append(password)
    print(*passwords, sep='\n')
