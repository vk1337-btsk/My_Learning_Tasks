from random import randint


def guess_digit():
    print('Укажите границу загадываемого числа')
    digit = randint(1, int(input()))
    print(digit)
    i = 0
    while True:
        n = input("Попробуйте угадать загаданное число: ")
        i += 1
        if not n.isdigit():
            print('А может быть все-таки введем целое число от 1 до 100?')
            i -= 1
            continue
        if int(n) < digit:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            continue
        if int(n) > digit:
            print('Ваше число больше загаданного, попробуйте еще разок')
            continue
        if int(n) == digit:
            print('Вы угадали, поздравляем!')
            break
    print('Вы угадали за ', i, "попыток.")
    print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
