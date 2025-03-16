import random


def spin_reels():
    symbols = ["🍒", "🍋", "🍊", "🍉", "⭐", "7", "🍇", "🍑"]
    return [[random.choice(symbols) for _ in range(4)] for _ in range(4)]

def check_cherries(row, bet):

    cherries_count = 0
    scater_count = 0
    winnings = 0

    for i in range(4):
        if row[i] == "🍒":
            cherries_count += 1
        elif row[i] == "7":
            cherries_count += 1
        elif row[i] == "⭐":
            scater_count += 1
        else:
            break


    if cherries_count == 4:
        winnings = bet * 20

    if cherries_count == 3:
        winnings = bet * 5

    if scater_count == 3:
        winnings += bet * 5

    elif scater_count == 4:
        winnings = bet * 20

    return winnings

def check_lemons(row, bet):

    lemons_count = 0
    scater_count = 0
    winnings = 0

    for i in range(4):
        if row[i] == "🍋":
            lemons_count += 1
        elif row[i] == "7":
            lemons_count += 1
        elif row[i] == "⭐":
            scater_count += 1
        else:
            break


    if lemons_count == 4:
        winnings = bet * 20

    if lemons_count == 3:
        winnings = bet * 5

    if scater_count == 3:
        winnings += bet * 5

    elif scater_count == 4:
        winnings = bet * 20

    return winnings

def check_orange(row, bet):

    orange_count = 0
    scater_count = 0
    winnings = 0


    for i in range(4):
        if row[i] == "🍊":
            orange_count += 1
        elif row[i] == "7":
            orange_count += 1
        elif row[i] == "⭐":
            scater_count += 1
        else:
            break


    if orange_count == 4:
        winnings = bet * 20

    if orange_count == 3:
        winnings = bet * 5

    if scater_count == 3:
        winnings += bet * 5

    elif scater_count == 4:
        winnings = bet * 20

    return winnings

def check_watermelon(row, bet):

    waterMelon_count = 0
    scater_count = 0
    winnings = 0


    for i in range(4):
        if row[i] == "🍉":
            waterMelon_count += 1
        elif row[i] == "7":
            waterMelon_count += 1
        elif row[i] == "⭐":
            scater_count += 1
        else:
            break


    if waterMelon_count == 4:
        winnings = bet * 30

    if waterMelon_count == 3:
        winnings = bet * 10

    if scater_count == 3:
        winnings += bet * 5

    elif scater_count == 4:
        winnings = bet * 20

    return winnings

def check_grapes(row, bet):

    grapes_count = 0
    scater_count = 0
    winnings = 0


    for i in range(4):
        if row[i] == "🍇":
            grapes_count += 1
        elif row[i] == "7":
            grapes_count += 1
        elif row[i] == "⭐":
            scater_count += 1
        else:
            break


    if grapes_count == 4:
        winnings = bet * 30

    if grapes_count == 3:
        winnings = bet * 10

    if scater_count == 3:
        winnings += bet * 5

    elif scater_count == 4:
        winnings = bet * 20

    return winnings

def check_plums(row, bet):

    plums_count = 0
    scater_count = 0
    winnings = 0


    for i in range(4):
        if row[i] == "🍑":
            plums_count += 1
        elif row[i] == "7":
            plums_count += 1
        elif row[i] == "⭐":
            scater_count += 1
        else:
            break


    if plums_count == 4:
        winnings = bet * 20

    if plums_count == 3:
        winnings = bet * 5

    if scater_count == 3:
        winnings += bet * 5

    elif scater_count == 4:
        winnings = bet * 20

    return winnings

def check_7(row, bet):

    seven_count = 0
    scater_count = 0
    winnings = 0


    for i in range(4):
        if row[i] == "7":
            seven_count += 1
        elif row[i] == "⭐":
            scater_count += 1
        else:
            break


    if seven_count == 4:
        winnings = bet * 200

    if seven_count == 3:
        winnings = bet * 20

    if scater_count == 3:
        winnings += bet * 5

    elif scater_count == 4:
        winnings = bet * 20

    return winnings


def check_winnings(reels, bet):
    winnings = 0
    for row in reels:
        # Проверка за череши на всеки ред
        winnings += check_cherries(row, bet)
        winnings += check_lemons(row, bet)
        winnings += check_orange(row, bet)
        winnings += check_watermelon(row, bet)
        winnings += check_grapes(row, bet)
        winnings += check_plums(row, bet)
        winnings += check_7(row, bet)

        # Можеш да добавиш още проверки за други символи тук

    return winnings


def print_reels(reels):
    for row in reels:
        print(" | ".join(row))


def play_game():
    balance = int(input("Въведете начален баланс: "))  # Начален баланс
    print("Вашият баланс е:", balance)

    while balance > 0:
        try:
            bet = int(input("Въведете залог: "))
            if bet == 0:
                print("Напускате играта с баланс:", balance)
                break
            if bet > balance or bet <= 0:
                print("Невалиден залог!")
                continue
        except ValueError:
            print("Моля, въведете число!")
            continue

        balance -= bet  # Намаляване на баланса със залога
        reels = spin_reels()
        print("Резултат:")
        print_reels(reels)

        # Изчисляване на печалбите
        winnings = check_winnings(reels, bet)

        if winnings > 0:
            print(f"Поздравления! Спечелихте {winnings}!")
            balance += winnings
        else:
            print("Няма печалба. Опитайте пак!")

        print("Текущ баланс:", balance)

    print("Край на играта!")


if __name__ == "__main__":
    play_game()
