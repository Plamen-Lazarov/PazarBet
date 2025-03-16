import random

def spin_reels():
    #1 - cherry
    #2 - lemon
    #3 - orange
    #4 - watermelon
    #5 - scater
    #6 - grape
    #7 - seven
    #8 - plum

    
    symbols = [1, 2, 3, 4, 5, 6, 7, 8]
    return [[random.choice(symbols) for _ in range(4)] for _ in range(4)]

def check_cherries(row, bet):
    cherries_count = 0
    scater_count = 0
    winnings = 0

    for i in range(4):
        if row[i] == 1:
            cherries_count += 1
        elif row[i] == 7:
            cherries_count += 1
        elif row[i] == 5:
            scater_count += 1
        else:
            break

    if cherries_count == 4:
        winnings = bet * 20
    elif cherries_count == 3:
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
        if row[i] == 2:
            lemons_count += 1
        elif row[i] == 7:
            lemons_count += 1
        elif row[i] == 5:
            scater_count += 1
        else:
            break

    if lemons_count == 4:
        winnings = bet * 20
    elif lemons_count == 3:
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
        if row[i] == 3:
            orange_count += 1
        elif row[i] == 7:
            orange_count += 1
        elif row[i] == 5:
            scater_count += 1
        else:
            break

    if orange_count == 4:
        winnings = bet * 20
    elif orange_count == 3:
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
        if row[i] == 4:
            waterMelon_count += 1
        elif row[i] == 7:
            waterMelon_count += 1
        elif row[i] == 5:
            scater_count += 1
        else:
            break

    if waterMelon_count == 4:
        winnings = bet * 30
    elif waterMelon_count == 3:
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
        if row[i] == 6:
            grapes_count += 1
        elif row[i] == 7:
            grapes_count += 1
        elif row[i] == 5:
            scater_count += 1
        else:
            break

    if grapes_count == 4:
        winnings = bet * 30
    elif grapes_count == 3:
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
        if row[i] == 8:
            plums_count += 1
        elif row[i] == 7:
            plums_count += 1
        elif row[i] == 5:
            scater_count += 1
        else:
            break

    if plums_count == 4:
        winnings = bet * 20
    elif plums_count == 3:
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
        if row[i] == 7:
            seven_count += 1
        elif row[i] == 5:
            scater_count += 1
        else:
            break

    if seven_count == 4:
        winnings = bet * 200
    elif seven_count == 3:
        winnings = bet * 20

    if scater_count == 3:
        winnings += bet * 5
    elif scater_count == 4:
        winnings = bet * 20

    return winnings

def check_winnings(reels, bet):
    winnings = 0
    for row in reels:
        winnings += check_cherries(row, bet)
        winnings += check_lemons(row, bet)
        winnings += check_orange(row, bet)
        winnings += check_watermelon(row, bet)
        winnings += check_grapes(row, bet)
        winnings += check_plums(row, bet)
        winnings += check_7(row, bet)

    return winnings

def print_reels(reels):
    for row in reels:
        print(" | ".join(str(x) for x in row))

def play_game():
    balance = int(input("Enter opening balance: "))
    print("Your balance is:", balance)

    while balance > 0:
        try:
            bet = int(input("Enter a bet: "))
            if bet == 0:
                print("You leave the game with a balance:", balance)
                break
            if bet > balance or bet <= 0:
                print("Invalid bet!")
                continue
        except ValueError:
            print("Please, enter a number!")
            continue

        balance -= bet
        reels = spin_reels()
        print("Result:")
        print_reels(reels)

        winnings = check_winnings(reels, bet)

        if winnings > 0:
            print(f"Congratulations! You win {winnings}!")
            balance += winnings
        else:
            print("No win. Try again!")

        print("Current balance:", balance)

    print("Game over!")

play_game()
