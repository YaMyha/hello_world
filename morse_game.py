import random
import keyboard


morse_dict = {
  "0": "-----",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": "..-.",
  "g": "--.",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--..",
  ".": ".-.-.-",
  ",": "--..--",
  "?": "..--..",
  "!": "-.-.--",
  "-": "-....-",
  "/": "-..-.",
  "@": ".--.-.",
  "(": "-.--.",
  ")": "-.--.-"
}

def morse_encode(word):
    res = ''
    for char in [*word]:
        res += morse_dict[char]
    return res


def get_word():
    return words_eng[random.randint(0, len(words_eng)-1)]
    

def print_statictics():
    print("""
          Всего задачек: {value_1}
          Отвечено верно: {value_2}
          Отвечено неверно: {value_3}
          """.format(value_1 = len(ans), value_2 = ans.count(True), value_3 = ans.count(False)))
    
    
ans = []   
words_eng = ['python', 'basik', 'keyboard', 'side', 'worth', 'drive']
print("""Сегодня мы потренируемся расшифровывать морзянку.
Нажмите Enter и начнем""")
keyboard.wait('Enter')
input()
while True:
    iter_word = get_word()
    print(f'Переведите слово: {iter_word} на азбуку Морзе.')
 
    response = input('Введите код:')
    if response == 'Стоп':
        break
    while response != morse_encode(iter_word):
                    
        for char in [*response]:
            if char not in ['-', '.']:
                print('Введенный код не является кодом на азбуке Морзе!')
                break
            else:
                print('Что-то не так. Попробуй ещё раз...')
        response = input('Введите код:')
    print('Молодец! Это правильный ответ!')  

        
print_statictics()
