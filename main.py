from random import *


# заменить запись слов не в список а в файл!
def generate_word():
    words = ["космос", "орбита", "армия", "школа", "работа", "бизнес"]
    return choice(words)

# попыток 6
def update_game(step):
    step6 = ("----------------\n"
             "       |      ||\n"
             "              ||\n"
             "              ||\n"
             "              ||\n"
             "================\n"
             "=================\n"
             )
    step5 = ("----------------\n"
             "       |      ||\n"
             "       0      ||\n"
             "              ||\n"
             "              ||\n"
             "================\n"
             "=================\n"
             )
    step4 = ("----------------\n"
             "       |      ||\n"
             "       0      ||\n"
             "       О      ||\n"
             "              ||\n"
             "================\n"
             "=================\n"
             )
    step3 = ("----------------\n"
             "       |      ||\n"
             "       0      ||\n"
             "       О\     ||\n"
             "              ||\n"
             "================\n"
             "=================\n"
             )
    step2 = ("----------------\n"
             "       |      ||\n"
             "       0      ||\n"
             "      /О\     ||\n"
             "              ||\n"
             "================\n"
             "=================\n"
             )
    step1 = ("----------------\n"
             "       |      ||\n"
             "       0      ||\n"
             "      /О\     ||\n"
             "      /       ||\n"
             "================\n"
             "=================\n"
             )
    step0 = ("----------------\n"
             "       |      ||\n"
             "       0      ||\n"
             "      /О\\     ||\n"
             "      / \\     ||\n"
             "================\n"
             "=================\n"
             )
    steps = [step0, step1, step2, step3, step4, step5, step6]

    return print(*steps[step])


def game():
    while True:
        lifes = 7
        win_word = list(generate_word())
        display_word = list("_"*len(win_word))
        print("привет игрок + тут какую-нибудь подводку надо сделать "
              " + правила игры")

        while True:
            if "_" not in display_word and lifes > 0:
                print("УРА ПОБЕДА ТЫ УГАДАЛ СЛОВО: ", *display_word)
                print("тут придумать как человечек убегает с виселицы")
                input("для начала новой игры нажми ENTER")
                break
            elif lifes == 0:
                print("К СОЖАЛЕНИЮ ВЫ ПРОИГРАЛИ :(")
                print("ЗАГАДАННЫМ СЛОВОМ БЫЛО: ", win_word)
                input("для начала новой игры нажми ENTER")
                break
            print(f"СЛОВО: ", *display_word)
            player_letter = input("ТВОЯ БУКВА: \n")

            if player_letter in win_word:
                for i in range(len(win_word)):
                    if win_word[i] == player_letter: display_word[i] = player_letter
            else:
                lifes -= 1
                update_game(lifes)


game()
