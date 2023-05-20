import json


def max_column(jsn: dict) -> int:
    return max([len(i) for i in jsn.keys()])


def check_question(jsn: dict, user_choice: list):
    return jsn[user_choice[0]][user_choice[1]]


def choose_question(jsn: dict):
    max_len = max_column(jsn)

    for subject, item in jsn.items():
        print(f"{subject.ljust(max_len)}", end='')
        for value in item.keys():
            if not jsn[subject][value]["asked"]:
                print(f" {value.ljust(5)}", end='')
            else:
                print('    '.ljust(5), end='')
        print('\n')

    while True:
        try:
            user_choice = input('Выберите вопрос:').split()
            if check_question(jsn, user_choice):
                break
        except Exception:
            print('Такого вопроса нет!')
            continue

    print(f'Как переводится слово: {jsn[user_choice[0]][user_choice[1]]["question"]}?')

    jsn[user_choice[0]][user_choice[1]]["asked"] = True

    return jsn, user_choice


def check_answer(jsn: dict, user_choice: list) -> int:
    if input('Ответ:') == jsn[user_choice[0]][user_choice[1]]["answer"]:
        print(f"Верно! +{user_choice[1]} очков!", end='')
        return int(user_choice[1])
    else:
        print('Неверно!')
        return -int(user_choice[1])


def record(name: str, score: int, right: int):
    with open("records.json", "r", encoding='utf-8') as jsn:
        results = json.load(jsn)

    results.append({name: {"points": score, "correct": right, "incorrect": count_questions() - right}})

    with open("records.json", "w", encoding='utf-8') as jsn:
        json.dump(results, jsn)


def count_questions():
    with open("questions.json", encoding='utf-8') as jsn:
        questions = json.load(jsn)
    return len(questions) * len(questions[list(questions)[0]])
