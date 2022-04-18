import random


def main():
    with open('files/words.txt') as f:
        lines = f.readlines()
    today_word = random.choice(lines)
    print(today_word)
    check = ''
    while check != today_word:
        guess = input('Введите слово из 5 букв: ')
        if len(guess) < 5:
            continue
        check = suspicion(today_word, guess)
        if check == today_word:
            print('вы угадали!')
            break
        else:
            print(check)


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