import random
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt

with open('files/words.txt') as f:
    lines = [x.strip() for x in f.readlines()]

LINES = lines


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('files/wordle.ui', self)
        self.b1 = [self.pushButton, self.pushButton_2, self.pushButton_3, self.pushButton_4, self.pushButton_5]
        self.b2 = [self.pushButton_6, self.pushButton_7, self.pushButton_8, self.pushButton_9, self.pushButton_10]
        self.b3 = [self.pushButton_11, self.pushButton_12, self.pushButton_13, self.pushButton_14, self.pushButton_15]
        self.b4 = [self.pushButton_16, self.pushButton_17, self.pushButton_18, self.pushButton_19, self.pushButton_20]
        self.b5 = [self.pushButton_21, self.pushButton_22, self.pushButton_23, self.pushButton_24, self.pushButton_25]
        self.count = 0
        self.flag = False
        self.readyButton.clicked.connect(self.run)
        self.today_word = random.choice(LINES).strip()
        print(self.today_word)
        self.kguess = ''

    def run(self):
        if self.count < 5 and not self.flag:
            guess = self.lineEdit.text()
            if len(guess) != 5 or guess not in LINES:
                print('слова нет в словаре')
            else:
                result, right_symbol = self.suspicion(guess)
                self.write_word(result, right_symbol)

                self.count += 1
            self.lineEdit.clear()

        else:
            print('вы исчерпали попытки')

    def write_word(self, res, right_symbol):
        if self.count == 0:
            target_group = self.b1
        elif self.count == 1:
            target_group = self.b2
        elif self.count == 2:
            target_group = self.b3
        elif self.count == 3:
            target_group = self.b4
        elif self.count == 4:
            target_group = self.b5
        for i in range(len(target_group)):
            if res[i] != '_':
                target_group[i].setStyleSheet('background: rgb(0,200,0);')
            elif target_group[i].text() in right_symbol:
                target_group[i].setStyleSheet('background: rgb(200,200,0);')
                right_symbol.remove(target_group[i].text())

    def keyReleaseEvent(self, event):
        if event.text() != '':
            self.kguess = self.lineEdit.text()
        if self.count == 0:
            target_group = self.b1
        elif self.count == 1:
            target_group = self.b2
        elif self.count == 2:
            target_group = self.b3
        elif self.count == 3:
            target_group = self.b4
        elif self.count == 4:
            target_group = self.b5
        for i in range(5):
            if len(self.kguess) - 1 >= i:
                target_group[i].setText(self.kguess[i])
            else:
                target_group[i].setText('')

    def suspicion(self, guess):
        true_symbol = []
        if guess == self.today_word:
            self.flag = True
            return guess, true_symbol
        res = ''
        for i in range(5):
            if self.today_word[i] == guess[i]:
                res += guess[i]
            else:
                if guess[i] in self.today_word:
                    true_symbol.append(guess[i])
                res += '_'
        for symb in true_symbol:
            if res.count(symb) == self.today_word.count(symb):
                true_symbol.remove(symb)
            if self.today_word.count(symb) < true_symbol.count(symb):
                true_symbol.remove(symb)
            if self.today_word.count(symb) < res.count(symb) + true_symbol.count(symb):
                true_symbol.remove(symb)
        return res, true_symbol


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
