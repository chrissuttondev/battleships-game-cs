from random import randint
import random
print("Welcome to Battleships")


def get_shot(guesses):
    """
    Prompts user to take a shot. Coverts shot to and integer.
    Validates input and prompts again if user input not valid. 
    """

    while True:
        try:
            shot = input("\nTake your shot: ")
            shot = int(shot)
            if shot < 0 or shot > 99:
                print("\nMiss-fire, choose number 0-99: ")
            elif shot in guesses:
                print("\nAlready fired there, guess again: ")
            else:
                break
        except:
            print("\nOoops miss-fire, try again: ")
    return shot

def show_board(hit, miss):
    """
    Displays game board in terminal. The board has 99 places.
    When a user takes a it will be indicated on the board wether 
    the shot was a hit (H) or a miss (M). 
    """
    print("\n        BATTLESHIPS")
    print("\n     0 1 2 3 4 5 6 7 8 9")

    place = 0
    for x in range(10):
        row = ""
        for ch in range(10):
            ch = " _"
            if place in miss:
                ch = " M"
            elif place in hit:
                ch = " H"

            row = row + ch
            place = place + 1
        print(x, " ", row)


def check_shot(shot, ships, hit, miss):
    """
    Checks if the users shot is a hit or a miss and appends the shot to
    a list held in a variables named hit and miss respectively.
    Prints a message to the terminal to inform user if shot a hit or a miss.
    """

    hit_msgs = ["You smashed 'em.",
                "Great Shot.",
                "Another one bites the dust.",
                "They're toast.",
                "They are fish food.",
                "Down it goes.",
                "The sharks feast tonight.",
                "Surfs up."]
    random.shuffle(hit_msgs)

    miss_msgs = ["Unlucky.",
                 "Keep trying",
                 "Better luck next time",
                 "What are you even aiming at?",
                 "Sheesh, miles off!",
                 "close one",
                 "You know your supposed hit the ships?",
                 "Stop wasting ammo!"]

    random.shuffle(miss_msgs)

    if shot in ships:
        ships.remove(shot)
        if len(ships) > -1:
            hit.append(shot)
            if hit_msgs:
                random_msg = hit_msgs.pop()
                print(f"\nDIRECT HIT!\n{random_msg}")
    else:
        miss.append(shot)
        if miss_msgs:
            random_msg = miss_msgs.pop()
            print(f"\nYOU MISSED!\n{random_msg}")
    return ships, hit, miss,


def run_game():
    """
    Calls the program functions to run the game.
    """

    ships = random.sample(range(0, 99), 5)
    print(ships)
    hit = []
    miss = []
    target_length = 20

    for i in range(20):
        show_board(hit, miss)
        guesses = hit + miss
        shot = get_shot(guesses)
        ships, hit, miss = check_shot(shot, ships, hit, miss)
        turns = hit + miss
        if not bool(ships):  # if ships list empty game end you win
            print("\nYOU WIN! ENEMY VESSELS DESTROYED")
            break
        player_lose(turns, target_length)


def player_lose(turns, target_length):
    """
    Checks the length of the list stored in the turns variable. 
    If the list has reached the target lenght thee game and ends 
    and the player loses as not all ships have been hit.
    """
    if len(turns) == target_length:
        print("\nYOU LOSE! ENEMY THREAT REMAINS")
