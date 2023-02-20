from flask import Flask
import json


def find_skill(skill):
    list_of_cand = []
    for one in candidates:
        if skill in one["skills"].lower().split(", "):
            list_of_cand.append(candidates.index(one))
    return list_of_cand


with open("candidates.json", encoding='utf-8') as jsn:
    candidates = json.load(jsn)

app = Flask(__name__)


@app.route('/')
def page_main():
    res = '<pre>\n'

    for i in candidates:
        res += f"""{i["name"]} -
{i["position"]}
{i["skills"]}\n\n"""
    res += "</pre>"
    return res


@app.route('/candidate/<int:x>')
def page_candidate(x):
    res = f'<img src ="({candidates[x - 1]["picture"]})">\n\n<pre>\n'

    res += f"""{candidates[x - 1]["name"]} -
{candidates[x - 1]["position"]}
{candidates[x - 1]["skills"]}\n"""
    res += "</pre>"
    return res


@app.route("/skill/<skill>")
def page_skill(skill):
    res = '<pre>\n'

    for i in find_skill(skill):
        res += f"""{candidates[i]["name"]} -
{candidates[i]["position"]}
{candidates[i]["skills"]}\n\n"""
    res += "</pre>"
    return res


app.run(debug=True)
