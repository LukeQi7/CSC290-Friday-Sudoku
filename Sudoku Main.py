"""
=== Module Description ===
This module contains the main function that runs the game.
"""
from board import Board

if __name__ == "__main__":
    s = Board()
    while not s.is_full():
        print(s.nice_string())
        lst = s.get_user_input()
        x = lst[0]
        y = lst[1]
        value = lst[2]
        if s.get_penciled(x, y, value) is True:
            print("Setting", x, ",", y, " to", value)
            s.change_val(x, y, value)
        else:
            print("Penciling", value, " at", x, ",", y)
            s.set_penciled(x, y, value, True)

    if s.is_won():
        print("Game Won!")
    else:
        print("Game Lost!")
