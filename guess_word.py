import random

name = input('Введите Ваше имя:')
record = 0

with open("words.txt", "rt") as w:
    for line in w:
        word = line.rstrip("\n")
        mesh = [*word]
        random.shuffle(mesh)
        mesh = ''.join(mesh)
        print(f"Угадайте слово: {mesh}")
        if input() == word:
            print('Правильный ответ! Вы получаете 10 очков.')
            record += 10
        else:
            print(f'Неверно. Верный ответ - {word}')

with open("history.txt", "a") as h:
    h.write(f"{name}  {record}\n")

with open("history.txt", "rt") as h:
    max = 0
    count = 0
    for record in h:
        temp = int(record.split('  ')[1])
        if temp > max:
            max = temp
        count += 1

    print(f"""Всего игр сыграно: {count}.
Максимальный рекорд: {max}""")
