from utils import guess_digit


def start():
    print('Добро пожаловать в числовую угадайку')

    while True:
        guess_digit()
        while True:
            print("Желаете попробовать снова? ")
            s = input("Да или нет? ")
            if s.lower() == "да":
                guess_digit()
            elif s.lower() == "нет":
                break
            else:
                continue


if __name__ == "__main__":
    start()
