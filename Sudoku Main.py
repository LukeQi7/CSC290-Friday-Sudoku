while game.iswon() is not True:
    x = raw_input("Row: ")
    y = raw_input("Column: ")
    value = raw_input("Number: ")
    if game.pencil_in is True:
        game.input(x, y, value)
    else:
        game.pencil_input(x, y, value)

print("Game Won!")
