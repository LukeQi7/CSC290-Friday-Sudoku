from board import Board
s = Board()

while not s.is_full():
    print(s.nice_string())
    x = int(input("Row: "))
    y = int(input("Column: "))
    value = int(input("Number: "))
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
