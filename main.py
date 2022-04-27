import random
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

with open('files/words.txt') as f:
    lines = [x.strip() for x in f.readlines()]

LINES = lines


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('files/wordle.ui', self)
        self.b1 = [self.pushButton, self.pushButton_2, self.pushButton_3, self.pushButton_4, self.pushButton_5]
        self.count = 0
        self.flag = False
        self.readyButton.clicked.connect(self.run)
        self.today_word = random.choice(LINES).strip()
        print(self.today_word)

    def run(self):
        if self.count < 5 and not self.flag:
            guess = self.lineEdit.text()
            if len(guess) != 5 or guess not in LINES:
                print('слова нет в словаре')
            elif guess == self.today_word:
                self.flag = True
                print('вы угадали!')
            else:
                result, right_symbol = suspicion(self.today_word, guess)
                self.write_word(result)
                print(result)
                if len(right_symbol) > 0:
                    print('Кроме того, в слове есть буквы:', *right_symbol)
            self.count += 1
            self.lineEdit.clear()

        else:
            print('вы исчерпали попытки')

    def write_word(self, res):
        if self.count == 0 or self.count == 1:
            target_group = self.b1
            print(self.count)
            print(target_group)
            for i in range(len(target_group)):
                if res[i] != '_':
                    target_group[i].setStyleSheet('background: rgb(0,200,0);')
                    target_group[i].setText(res[i])


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
