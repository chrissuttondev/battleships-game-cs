print("Welcome to Battleships")

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