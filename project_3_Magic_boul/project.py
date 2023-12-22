from utils import get_random_answer


if __name__ == "__main__":
    print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
    name = input('Как тебя зовут? ')
    print("Привет ", name)

    while True:
        question = input("Задайте свой вопрос: ")
        if not question:
            print("Вы не задали вопрос...")
            continue

        print(get_random_answer())

        if input("Желаете задать ещё один вопрос? ") in ("да", "Да"):
            continue
        else:
            print('Возвращайся если возникнут вопросы!')
            break
