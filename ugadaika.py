import json
import random


class Question:
    def __init__(self, text, complexity, answer, user_answer=None):
        self.text = text
        self.complexity = complexity
        self.answer = answer

        self.asked = False
        self.user_answer = user_answer
        self.points = 10 * int(self.complexity)

    def get_points(self):
        ''' Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 - 50 баллов.
        '''
        return self.points

    def is_correct(self):
        ''' Возвращает True, если ответ пользователя совпадает
        с верным ответом, иначе False.
        '''
        if self.user_answer == self.answer:
            return True
        else:
            return False

    def build_question(self):
        ''' Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: Что люди обычно называют американским флагом?
        Сложность 4/5'''
        return {'question': self.text, 'complexity': self.complexity}

    def build_positive_feedback(self):
        ''' Возвращает: "Ответ верный!"'''
        return f'Ответ верный! Получено {self.points} баллов.'

    def build_negative_feedback(self):
        ''' Возвращает: "Ответ неверный!"'''
        return f'Ответ неверный! Верный ответ - {self.answer}'


def get_statistics(list_):
    right_ans = 0
    score = 0
    for que in list_:
        right_ans += que.is_correct()
        if que.is_correct():
            score += que.get_points()

    print(f"""Вот и все!
Отвечено правильно: {right_ans}
Набрано очков: {score}""")


# def choose_random(dict):
#     return random.randint(1, len(questions))
def create_list():
    list_of_quest = []

    with open("questions.json", "r", encoding="utf-8") as f:
        q = json.load(f)

        for one in q:
            list_of_quest.append(Question(one["q"], one["d"], one["a"]))
    return list_of_quest


questions = create_list()
random.shuffle(questions)
for q in questions:
    q.user_answer = input(f'{q.build_question()["question"]}\nСложность: {q.build_question()["complexity"]}/5')
    q.asked = True
    if q.is_correct():
        print(q.build_positive_feedback())
    else:
        print(q.build_negative_feedback())

get_statistics(questions)
