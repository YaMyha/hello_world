import json
import utils

score = 0
right = 0


def start():
    global score
    global right

    name = input("Введите имя:")

    with open("questions.json", encoding='utf-8') as jsn:
        questions = json.load(jsn)

    for attempt in range(utils.count_questions()):
        questions, user_choice = utils.choose_question(questions)

        ans_score = utils.check_answer(questions, user_choice)

        # print(ans_score)
        # print(score, right)
        if ans_score:
            score += ans_score
            right += 1

        print(f" Ваш счет: {score}")
    return name


name = start()

print(f"""Раунд завершен!
Ваш счет: {score}
Верных ответов: {right}
Неверных ответов: {utils.count_questions() - right}""")

utils.record(name, score, right)
