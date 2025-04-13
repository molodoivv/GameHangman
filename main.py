from random import *


# заменить запись слов не в список а в файл!
def generate_word():
    words = ["космос", "орбита", "армия", "школа", "работа", "бизнес"]
    return choice(words)

# попыток 6
def update_game():
    pass


def game():
    lifes = 6
    win_word = generate_word()
    display_word = ["_"*len(win_word)]
    print("привет игрок + тут какую-нибудь подводку надо сделать + правила игры")

    while True:
        player_word = input("ТВОЯ БУКВА: \n")

        if player_word in win_word:
            for i in range(len(win_word)):
                if win_word[i] == player_word:
                    display_word[i] = player_word
        else:
            lifes -= 1
            print("такой буквы нет в слове") # тут нужно добавлять часть тела на виселице
