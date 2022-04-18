import random


def main():
    with open('files/words.txt') as f:
        lines = f.readlines()
    today_word = random.choice(lines).strip()
    print(today_word)
    while True:
        guess = input('Введите слово из 5 букв: ')
        if len(guess) < 5:
            continue
        if guess == today_word:
            print('вы угадали!')
            break
        else:
            print(suspicion(today_word, guess))


def suspicion(today_word, guess):
    res = ''
    for i in range(5):
        if today_word[i] == guess[i]:
            res += guess[i]
        else:
            res += '_'
    return res


if __name__ == '__main__':
    main()