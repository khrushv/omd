# Guido van Rossum <guido@python.org>
from random import randrange


def step1():
    print(
        'Утка-тива 🦆 🕵️ срочно вызывают расследовать дело в ААА, '
        'у одного из учеников не получается домашка и'
        'нужно помочь и разобрать ошибки. Выезжаем?'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_start()
    return step2_stay()


def step2_start():
    score = 0
    questions = {"Допускается ли  в коде множество длинных строк,"
                 " и использование табов?.":
                     {'a': ('\na. Ничего страшного, можно и так оставить. ', False),
                      'b': ('\nb. Сокращаем до 99 символов строки и делаем 4 пробела', True),
                      'c': ('\nc. Можно сократить до 77 символов '
                            'и заменить табуляцию на 4 пробела', True)},
                 "Утка-тив заметил, что ученик пытается сравнить 2 переменные "
                 "типа float, можно ли так делать?":
                     {'a': ('\na. Да, ведь числа можно сравнивать между собой', False),
                      'b': ('\nb. Нет, ведь некоторая точность теряется', True)},
                 "Является ли set упорядоченным?":
                     {'a': ('\na. Да', False), 'b': ('\nb. Нет', True)},
                 "Почему python называется именно так? ": {
                     'a': ('\na. Название пошло от семейства пресмыкающихся', False),
                     'b': ('\nb. Назвали в честь британского телешоу', True)}}
    for question, answer_options in questions.items():
        user_choice = ''
        while user_choice not in answer_options.keys():
            print(question)
            for answer in answer_options.values():
                print(answer[0])
            print('Выберите один из вариантов: ', *answer_options)
            user_choice = input()
        if answer_options[user_choice][1]:
            score += 1
    print("Количество правильных ответов: ", score)
    return step3_web()


def step2_stay():
    print(
        'Осудительное кря-кря-кря 🦆, '
        'Утка-тив является одним из менторов ААА, а как известно менторы в '
        'ААА призваны бороться с проблемами, а не избегать их.'
        'Но у тебя есть шанс одуматься.'
    )
    return step1()


def step3_web():
    print('Двигаемся дальше, наши кураторы сообщили о том, что некоторые студенты не могут включить вебкамеры,'
          'поэтому нужно помочь им и включить их, для этого нужно написать их номер'
          '(X - выключенная,O - включенная), когда закончите введите #')
    student_cameras = []
    number_of_students = 5
    for i in range(number_of_students):
        if not randrange(2):
            student_cameras.append('X')
        else:
            student_cameras.append('O')
    user_choice = ''
    while user_choice != '#':
        print(student_cameras)
        user_choice = input("Введите порядковый номер студента(с нуля): ")
        try:
            is_camera_turned_on = student_cameras[int(user_choice)] == 'O'
        except (IndexError, ValueError):
            continue
        if is_camera_turned_on:
            student_cameras[int(user_choice)] = 'X'
        else:
            student_cameras[int(user_choice)] = 'O'
    all_cameras_turned_on = True
    for student_camera in student_cameras:
        if student_camera == 'X':
            all_cameras_turned_on = False
            break
    if all_cameras_turned_on:
        print("Спасибо, Утка-тив 🦆 🕵️, вы успешно крякнули все камеры!")
    else:
        print("Некоторые камеры остались выключенными, точно ли вы Утка-тив?")

    print("Отлична работа, Утка-тив, теперь отправляйтесь на заслуженный отдых 🍻😎🍻")


if __name__ == '__main__':
    step1()
