import random
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('files/wordle.ui', self)
        self.run()

    def run(self):
        pass


def main():
    with open('files/words.txt') as f:
        lines = [x.strip() for x in f.readlines()]
    today_word = random.choice(lines).strip()
    print(today_word)
    for _ in range(5):
        guess = input('Введите слово из 5 букв: ')
        if len(guess) != 5 or guess not in lines:
            continue
        if guess == today_word:
            print('вы угадали!')
            break
        else:
            result, right_symbol = suspicion(today_word, guess)
            print(result)
            if len(right_symbol) > 0:
                print('Кроме того, в слове есть буквы:', *right_symbol)


def suspicion(today_word, guess):
    true_symbol = []
    res = ''
    for i in range(5):
        if today_word[i] == guess[i]:
            res += guess[i]
        else:
            if guess[i] in today_word:
                true_symbol.append(guess[i])
            res += '_'
    for symb in true_symbol:
        if res.count(symb) == today_word.count(symb):
            true_symbol.remove(symb)
        if today_word.count(symb) < true_symbol.count(symb):
            true_symbol.remove(symb)
        if today_word.count(symb) < res.count(symb) + true_symbol.count(symb):
            true_symbol.remove(symb)
    return res, true_symbol


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
