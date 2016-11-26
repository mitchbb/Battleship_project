import random

def overlap(a, b, x, y):
    for c in a:
        for u in x:
            if c == u:
                for d in b:
                    for v in y:
                        if d == v:
                            return True
    return False

def battleship():
    c_ship1_row = []
    c_ship1_col = []
    c_ship2_row = []
    c_ship2_col = []
    c_ship3_row = []
    c_ship3_col = []
    c_ship4_row = []
    c_ship4_col = []
    c_ship5_row = []
    c_ship5_col = []
    p_board = []
    c_board = []
    for i in range(10):
        p_board.append(["O"]*10)
    for i in range(10):
        c_board.append(["O"]*10)
    def print_board(board):
         for row in board:
            print " ".join(row)
    # Computer Ship Placement
    # 0 is horizaontal, 1 is vertical
    hovcs = random.randint(0, 1)
    if hovcs == 0:
        c_ship1_row.append(random.randint(1, 10))
        c_ship1_col_start = random.randint(3, 8)
        c_ship1_col.append(c_ship1_col_start - 2)
        c_ship1_col.append(c_ship1_col_start - 1)
        c_ship1_col.append(c_ship1_col_start)
        c_ship1_col.append(c_ship1_col_start + 1)
        c_ship1_col.append(c_ship1_col_start + 2)
    elif hovcs == 1:
        c_ship1_col.append(random.randint(1, 10))
        c_ship1_row_start = random.randint(3, 8)
        c_ship1_row.append(c_ship1_row_start - 2)
        c_ship1_row.append(c_ship1_row_start - 1)
        c_ship1_row.append(c_ship1_row_start)
        c_ship1_row.append(c_ship1_row_start + 1)
        c_ship1_row.append(c_ship1_row_start + 2)
    if hovcs == 0:
        c_ship1_col.append(42)
    else:
        c_ship1_row.append(42)
    hovcs = random.randint(0, 1)
    if hovcs == 0:
        c_ship2_row.append(random.randint(1, 10))
        c_ship2_col_start = random.randint(3, 9)
        c_ship2_col.append(c_ship2_col_start - 2)
        c_ship2_col.append(c_ship2_col_start - 1)
        c_ship2_col.append(c_ship2_col_start)
        c_ship2_col.append(c_ship2_col_start + 1)
    elif hovcs == 1:
        c_ship2_col.append(random.randint(1, 10))
        c_ship2_row_start = random.randint(3, 9)
        c_ship2_row.append(c_ship2_row_start - 2)
        c_ship2_row.append(c_ship2_row_start - 1)
        c_ship2_row.append(c_ship2_row_start)
        c_ship2_row.append(c_ship2_row_start + 1)
    if overlap(c_ship1_row, c_ship1_col, c_ship2_row, c_ship2_col) == True:
        print "a"
        battleship()
    if hovcs == 0:
        c_ship2_col.append(42)
    else:
        c_ship2_row.append(42)
    hovcs = random.randint(0, 1)
    if hovcs == 0:
        c_ship3_row.append(random.randint(1, 10))
        c_ship3_col_start = random.randint(2, 9)
        c_ship3_col.append(c_ship3_col_start - 1)
        c_ship3_col.append(c_ship3_col_start)
        c_ship3_col.append(c_ship3_col_start + 1)
    elif hovcs == 1:
        c_ship3_col.append(random.randint(1, 10))
        c_ship3_row_start = random.randint(2, 9)
        c_ship3_row.append(c_ship3_row_start - 1)
        c_ship3_row.append(c_ship3_row_start)
        c_ship3_row.append(c_ship3_row_start + 1)
    if overlap(c_ship1_row, c_ship1_col, c_ship3_row, c_ship3_col) == True:
        print "b"
        battleship()
    if overlap(c_ship3_row, c_ship3_col, c_ship2_row, c_ship2_col) == True:
        print "c"
        battleship()
    if hovcs == 0:
        c_ship3_col.append(42)
    else:
        c_ship3_row.append(42)
    hovcs = random.randint(0, 1)
    if hovcs == 0:
        c_ship4_row.append(random.randint(1, 10))
        c_ship4_col_start = random.randint(2, 9)
        c_ship4_col.append(c_ship4_col_start - 1)
        c_ship4_col.append(c_ship4_col_start)
        c_ship4_col.append(c_ship4_col_start + 1)
    elif hovcs == 1:
        c_ship4_col.append(random.randint(1, 10))
        c_ship4_row_start = random.randint(2, 9)
        c_ship4_row.append(c_ship4_row_start - 1)
        c_ship4_row.append(c_ship4_row_start)
        c_ship4_row.append(c_ship4_row_start + 1)
    if overlap(c_ship1_row, c_ship1_col, c_ship4_row, c_ship4_col) == True:
        print "d"
        battleship()
    if overlap(c_ship3_row, c_ship3_col, c_ship4_row, c_ship4_col) == True:
        print "e"
        battleship()
    if overlap(c_ship4_row, c_ship4_col, c_ship2_row, c_ship2_col) == True:
        print "f"
        battleship()
    if hovcs == 0:
        c_ship4_col.append(42)
    else:
        c_ship4_row.append(42)
    hovcs = random.randint(0, 1)
    if hovcs == 0:
        c_ship5_row.append(random.randint(1, 10))
        c_ship5_col_start = random.randint(2, 10)
        c_ship5_col.append(c_ship5_col_start - 1)
        c_ship5_col.append(c_ship5_col_start)

    elif hovcs == 1:
        c_ship5_col.append(random.randint(1, 10))
        c_ship5_row_start = random.randint(2, 10)
        c_ship5_row.append(c_ship5_row_start - 1)
        c_ship5_row.append(c_ship5_row_start)
    if overlap(c_ship1_row, c_ship1_col, c_ship5_row, c_ship5_col) == True:
        print "g"
        battleship()
    if overlap(c_ship3_row, c_ship3_col, c_ship5_row, c_ship5_col) == True:
        print "h"
        battleship()
    if overlap(c_ship4_row, c_ship4_col, c_ship5_row, c_ship5_col) == True:
        print "i"
        battleship()
    if overlap(c_ship5_row, c_ship5_col, c_ship2_row, c_ship2_col) == True:
        print "j"
        battleship()
    if hovcs == 0:
        c_ship5_col.append(42)
    else:
        c_ship5_row.append(42)
    # Player ship placement
    t = 0
    while t == 0:
        p_ship1_row = []
        p_ship1_col = []
        hovps = raw_input("Do you want your aircraft carrier to be horizontal or vertical? (Type 'H' or 'V'): ")
        if hovps == 'V':
            x = int(raw_input("In what column do you want your ship? (1-10): "))
            if 1 > x or x > 10:
                print "Oops! Please enter a number between 1 and 10."
            else:
                p_ship1_col.append(x)
                y = int(raw_input("In what row do you want the center of your ship? (3-8): "))
                if 9 < y or y < 3:
                    print "Oops! Please enter a number between 3 and 8."
                else:
                    p_ship1_row.append(y - 2)
                    p_ship1_row.append(y - 1)
                    p_ship1_row.append(y)
                    p_ship1_row.append(y + 1)
                    p_ship1_row.append(y + 2)
                    for a in p_ship1_row:
                        for b in p_ship1_col:
                            p_board[a - 1][b - 1] = "A"
                    print_board(p_board)
                    p_ship1_row.append(42)
                    t = 1
        elif hovps == 'H':
            x = int(raw_input("In what row do you want your ship? (1-10): "))
            if 1 > x or x > 10:
                print "Oops! Please enter a number between 1 and 10."
            else:
                p_ship1_row.append(x)
                y = int(raw_input("In what column do you want the center of your ship? (3-8): "))
                if 1 > y or y > 10:
                    print "Oops! Please enter a number between 3 and 8."
                
                else:
                    p_ship1_col.append(y - 2)
                    p_ship1_col.append(y - 1)
                    p_ship1_col.append(y)
                    p_ship1_col.append(y + 1)
                    p_ship1_col.append(y + 2)
                    for a in p_ship1_row:
                        for b in p_ship1_col:
                            p_board[a - 1][b - 1] = "A"
                    print_board(p_board)
                    p_ship1_col.append(42)
                    t = 1
        else:
            print "Oops! Please enter either a capital 'H' or a capital 'V'."
    while t == 1:
        p_ship2_row = []
        p_ship2_col = []
        hovps = raw_input("Do you want your battleship to be horizontal or vertical? (Type 'H' or 'V'): ")
        if hovps == 'V':
            x = int(raw_input("In what column do you want your ship? (1-10): "))
            if 1 > x or x > 10:
                print "Oops! Please enter a number between 1 and 10."
            else:
                p_ship2_col.append(x)
                y = int(raw_input("In what row do you want the center of your ship? (3-9): "))
                if 3 > y or y > 9:
                    print "Oops! Please enter a number between 3 and 9."
                else:
                    p_ship2_row.append(y - 2)
                    p_ship2_row.append(y - 1)
                    p_ship2_row.append(y)
                    p_ship2_row.append(y + 1)
                    if overlap(p_ship1_row, p_ship1_col, p_ship2_row, p_ship2_col) == True:
                        print "Oops! It looks like your ships are overlapping. Let's try again."
                    else:
                        for a in p_ship2_row:
                            for b in p_ship2_col:
                                p_board[a - 1][b - 1] = "B"
                        print_board(p_board)
                        p_ship2_row.append(42)
                        t = 2
        elif hovps == 'H':
            x = int(raw_input("In what row do you want your ship? (1-10): "))
            if 1 > x or x > 10:
                print "Oops! Please enter a number between 1 and 10."
            else:
                p_ship2_row.append(x)
                y = int(raw_input("In what column do you want the center of your ship? (3-9): "))
                if 3 > y or y > 9:
                    print "Oops! Please enter a number between 3 and 9."
                else:
                    p_ship2_col.append(y - 2)
                    p_ship2_col.append(y - 1)
                    p_ship2_col.append(y)
                    p_ship2_col.append(y + 1)
                    if overlap(p_ship1_row, p_ship1_col, p_ship2_row, p_ship2_col) == True:
                        print "Oops! It looks like your ships are overlapping. Let's try again."
                    else:
                        for a in p_ship2_row:
                            for b in p_ship2_col:
                                p_board[a - 1][b - 1] = "B"
                        print_board(p_board)
                        p_ship2_col.append(42)
                        t = 2
                    
        else:
            print "Oops! Please enter either a capital 'H' or a capital 'V'."
    while t == 2:
        p_ship3_row = []
        p_ship3_col = []
        hovps = raw_input("Do you want your submarine to be horizontal or vertical? (Type 'H' or 'V'): ")
        if hovps == 'V':
            x = int(raw_input("In what column do you want your ship? (1-10): "))
            if 1 > x or x > 10:
                print "Oops! Please enter a number between 1 and 10."
            else:
                p_ship3_col.append(x)
                y = int(raw_input("In what row do you want the center of your ship? (2-9): "))
                if 2 > y or y > 9:
                    print "Oops! Please enter a number between 2 and 9."
                else:
                    p_ship3_row.append(y - 1)
                    p_ship3_row.append(y)
                    p_ship3_row.append(y + 1)                  
                    if overlap(p_ship1_row, p_ship1_col, p_ship3_row, p_ship3_col) == True:
                        print "Oops! It looks like your ships are overlapping. Let's try again"
                    elif overlap(p_ship3_row, p_ship3_col, p_ship2_row, p_ship2_col) == True:
                        print "Oops! It looks like your ships are overlapping. Let's try again"
                    else:
                        for a in p_ship3_row:
                            for b in p_ship3_col:
                                p_board[a - 1][b - 1] = "S"
                        print_board(p_board)
                        p_ship3_col.append(42)
                        t = 3
        elif hovps == 'H':
            x = int(raw_input("In what row do you want your ship? (1-10): "))
            if 1 > x or x > 10:
                print "Oops! Please enter a number between 1 and 10."
            else:
                p_ship3_row.append(x)
                y = int(raw_input("In what column do you want the center of your ship? (2-9): "))
                if 2 > y or y > 9:
                    print "Oops! Please enter a number between 2 and 9."
                else:
                    p_ship3_col.append(y - 1)
                    p_ship3_col.append(y)
                    p_ship3_col.append(y + 1)
                    if overlap(p_ship1_row, p_ship1_col, p_ship3_row, p_ship3_col) == True:
                        print "Oops! It looks like your ships are overlapping. Let's try again"
                    elif overlap(p_ship3_row, p_ship3_col, p_ship2_row, p_ship2_col) == True:
                        print "Oops! It looks like your ships are overlapping. Let's try again"
                    else:
                        for a in p_ship3_row:
                            for b in p_ship3_col:
                                p_board[a - 1][b - 1] = "S"
                        print_board(p_board)
                        p_ship3_col.append(42)
                        t = 3
        else:
            print "Oops! Please enter either a capital 'H' or a capital 'V'."
    while t == 3:
        p_ship4_row = []
        p_ship4_col = []
        hovps = raw_input("Do you want your destroyer to be horizontal or vertical? (Type 'H' or 'V'): ")
        if hovps == 'V':
            x = int(raw_input("In what column do you want your ship? (1-10): "))
            if 1 > x or x > 10:
                print "Oops! Please enter a number between 1 and 10."
            else:
                p_ship4_col.append(x)
                y = int(raw_input("In what row do you want the center of your ship? (2-9): "))
                if 2 > y or y > 9:
                    print "Oops! Please enter a number between 2 and 9."
                else:
                    p_ship4_row.append(y - 1)
                    p_ship4_row.append(y)
                    p_ship4_row.append(y + 1)
                    if overlap(p_ship1_row, p_ship1_col, p_ship4_row, p_ship4_col) == True:
                        print "Oops! It looks like your ships are overlapping. Let's try again"
                    elif overlap(p_ship4_row, p_ship4_col, p_ship2_row, p_ship2_col) == True:
                        print "Oops! It looks like your ships are overlapping. Let's try again"
                    elif overlap(p_ship3_row, p_ship3_col, p_ship4_row, p_ship4_col) == True:
                        print "Oops! It looks like your ships are overlapping. Let's try again"
                    else:
                        for a in p_ship4_row:
                            for b in p_ship4_col:
                                p_board[a - 1][b - 1] = "D"
                        print_board(p_board)
                        p_ship4_row.append(42)
                        t = 4
        elif hovps == 'H':
            x = int(raw_input("In what row do you want your ship? (1-10): "))
            if 1 > x or x > 10:
                print "Oops! Please enter a number between 1 and 10."
            else:
                p_ship4_row.append(x)
                y = int(raw_input("In what column do you want the center of your ship? (2-9): "))
                if 2 > y or y > 9:
                    print "Oops! Please enter a number between 2 and 9."
                else:
                    p_ship4_col.append(y - 1)
                    p_ship4_col.append(y)
                    p_ship4_col.append(y + 1)
                    if overlap(p_ship1_row, p_ship1_col, p_ship4_row, p_ship4_col) == True:
                        print "Oops! It looks like your ships are overlapping. Let's try again"
                    elif overlap(p_ship4_row, p_ship4_col, p_ship2_row, p_ship2_col) == True:
                        print "Oops! It looks like your ships are overlapping. Let's try again"
                    elif overlap(p_ship3_row, p_ship3_col, p_ship4_row, p_ship4_col) == True:
                        print "Oops! It looks like your ships are overlapping. Let's try again"
                    else:
                        for a in p_ship4_row:
                            for b in p_ship4_col:
                                p_board[a - 1][b - 1] = "D"
                        print_board(p_board)
                        p_ship4_col.append(42)
                        t = 4
        else:
            print "Oops! Please enter either a capital 'H' or a capital 'V'."
    while t == 4:
        p_ship5_row = []
        p_ship5_col = []
        hovps = raw_input("Do you want your patrol boat to be horizontal or vertical? (Type 'H' or 'V'): ")
        if hovps == 'V':
            x = int(raw_input("In what column do you want your ship? (1-10): "))
            if 1 > x or x > 10:
                print "Oops! Please enter a number between 1 and 10."
            else:
                p_ship5_col.append(x)
                y = int(raw_input("In what row do you want the center of your ship? (2-10): "))
                if 2 > y or y > 10:
                    print "Oops! Please enter a number between 2 and 10."
                else:
                    p_ship5_row.append(y - 1)
                    p_ship5_row.append(y)
                if overlap(p_ship5_row, p_ship5_col, p_ship4_row, p_ship4_col) == True:
                    print "Oops! It looks like your ships are overlapping. Let's try again"
                elif overlap(p_ship5_row, p_ship5_col, p_ship2_row, p_ship2_col) == True:
                    print "Oops! It looks like your ships are overlapping. Let's try again"
                elif overlap(p_ship3_row, p_ship3_col, p_ship5_row, p_ship5_col) == True:
                    print "Oops! It looks like your ships are overlapping. Let's try again"
                elif overlap(p_ship1_row, p_ship1_col, p_ship5_row, p_ship5_col) == True:
                    print "Oops! It looks like your ships are overlapping. Let's try again"
                else:
                    for a in p_ship5_row:
                        for b in p_ship5_col:
                            p_board[a - 1][b - 1] = "P"
                    print_board(p_board)
                    p_ship5_row.append(42)
                    t = 5
                    
        elif hovps == 'H':
            x = int(raw_input("In what row do you want your ship? (1-10): "))
            if 1 > x or x > 10:
                print "Oops! Please enter a number between 1 and 10."
            else:
                p_ship5_row.append(x)
                y = int(raw_input("In what column do you want the center of your ship? (2-10): "))
                if 2 > y or y > 10:
                    print "Oops! Please enter a number between 2 and 10."
                else:
                    p_ship5_col.append(y - 1)
                    p_ship5_col.append(y)
                    for a in p_ship5_row:
                        for b in p_ship5_col:
                            p_board[a - 1][b - 1] = "P"
                    print_board(p_board)
                    p_ship5_col.append(42)
                    t = 5
        else:
            print "Oops! Please enter either a capital 'H' or a capital 'V'."
    print p_ship1_row
    print p_ship1_col
    print p_ship2_row
    print p_ship2_col
    print p_ship3_row
    print p_ship3_col
    print p_ship4_row
    print p_ship4_col
    print p_ship5_row
    print p_ship5_col
    print c_ship1_row
    print c_ship1_col
    print c_ship2_row
    print c_ship2_col
    print c_ship3_row
    print c_ship3_col
    print c_ship4_row
    print c_ship4_col
    print c_ship5_row
    print c_ship5_col
        
    def p_guess():
        hom = 0
        p_guess_row = int(raw_input("Please enter a row for you guess (1-10): "))
        p_guess_col = int(raw_input("Please enter a column for you guess (1-10): "))
        for a in c_ship1_row:
            if a == p_guess_row:
                for b in c_ship1_col:
                    if b == p_guess_col:
                        print "You hit my aircraft carrier!"
                        c_board[p_guess_row - 1][p_guess_col - 1] = "X"
                        hom = 1
                        if len(c_ship1_row) > 1:
                            c_ship1_row.remove(p_guess_row)
                        elif len(c_ship1_col) > 1:
                            c_ship1_col.remove(p_guess_col)
                        if len(c_ship1_row) == 1 and len(c_ship1_col) == 1:
                            print "You sank my aircraft carrier!"
        for a in c_ship2_row:
            if a == p_guess_row:
                for b in c_ship2_col:
                    if b == p_guess_col:
                        print "You hit my battleship!"
                        c_board[p_guess_row - 1][p_guess_col - 1] = "X"
                        hom = 2
                        if len(c_ship2_row) > 1:
                            c_ship2_row.remove(p_guess_row)
                        elif len(c_ship2_col) > 1:
                            c_ship2_col.remove(p_guess_col)
                        if len(c_ship2_row) == 1 and len(c_ship2_col) == 1:
                            print "You sank my batteship!"
        for a in c_ship3_row:
            if a == p_guess_row:
                for b in c_ship3_col:
                    if b == p_guess_col:
                        print "You hit my submarine!"
                        c_board[p_guess_row - 1][p_guess_col - 1] = "X"
                        hom = 3
                        if len(c_ship3_row) > 1:
                            c_ship3_row.remove(p_guess_row)
                        elif len(c_ship3_col) > 1:
                            c_ship3_col.remove(p_guess_col)
                        if len(c_ship3_row) == 1 and len(c_ship3_col) == 1:
                            print "You sank my submarine!"
        for a in c_ship4_row:
            if a == p_guess_row:
                for b in c_ship4_col:
                    if b == p_guess_col:
                        print "You hit my destroyer!"
                        c_board[p_guess_row - 1][p_guess_col - 1] = "X"
                        hom = 4
                        if len(c_ship4_row) > 1:
                            c_ship4_row.remove(p_guess_row)
                        elif len(c_ship4_col) > 1:
                            c_ship4_col.remove(p_guess_col)
                        if len(c_ship4_row) == 1 and len(c_ship4_col) == 1:
                            print "You sank my destroyer!"
        for a in c_ship5_row:
            if a == p_guess_row:
                for b in c_ship5_col:
                    if b == p_guess_col:
                        print "You hit my patrol boat!"
                        c_board[p_guess_row - 1][p_guess_col - 1] = "X"
                        hom = 5
                        if len(c_ship5_row) > 1:
                            c_ship5_row.remove(p_guess_row)
                        elif len(c_ship5_col) > 1:
                            c_ship5_col.remove(p_guess_col)
                        if len(c_ship5_row) == 1 and len(c_ship5_col) == 1:
                            print "You sank my patrol boat!"
        if hom == 0:
            print "Miss!"
            if c_board[p_guess_row - 1][p_guess_col - 1] != "X":
                c_board[p_guess_row - 1][p_guess_col - 1] = "M"
        print_board(c_board)
    def c_guess():
        hom = 0
        while 1 < 2:
            c_guess_row = random.randint(1, 10)
            c_guess_col = random.randint(1, 10)
            if p_board[c_guess_row - 1][c_guess_col - 1] != "X" and p_board[c_guess_row - 1][c_guess_col - 1] != "M":
                if c_guess_row == 10 and c_guess_col == 10:
                    h = 0
                elif c_guess_row == 10 and c_guess_col == 1:
                    h = 0
                elif c_guess_row == 1 and c_guess_col == 10:
                    h = 0
                elif c_guess_row == 1 and c_guess_col == 1:
                    h = 0
                else:
                    break
        row = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        col = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for x in row:
            for y in col:
                # if (x, y) was a hit
                if p_board[x][y] == "X":                        
                    # if it's not on the edges
                    if x < 9 and x > 0 and y < 9 and y > 0:
                        # if the spaces around have not been hits, guess the space below
                        if p_board[x + 1][y] != "X" and p_board[x + 1][y] != "M" and p_board[x - 1][y] != "X" and p_board[x][y + 1] != "X" and p_board[x][y - 1] != "X":
                            c_guess_row = x + 2
                            c_guess_col = y + 1
                        # if the space below was a miss, and the others haven't been guessed
                        if p_board[x + 1][y] == "M" and p_board[x - 1][y] != "X" and p_board[x][y + 1] != "X" and p_board[x][y + 1] != "M" and p_board[x][y - 1] != "X":
                            # guess the space to the right
                            c_guess_row = x + 1
                            c_guess_col = y + 2
                        # if the spaces below and to the right were misses
                        if p_board[x + 1][y] == "M" and p_board[x][y + 1] == "M" and p_board[x - 1][y] != "M" and p_board[x - 1][y] != "X" and p_board[x][y - 1] != "X":
                            # guess the space above
                            c_guess_row = x
                            c_guess_col = y + 1
                        # if the spaces below, to the right, and above were misses
                        if p_board[x + 1][y] == "M" and p_board[x][y + 1] == "M" and p_board[x - 1][y] == "M" and p_board[x][y - 1] != "M" and p_board[x][y - 1] != "X":
                            # guess the space to the left
                            c_guess_row = x + 1
                            c_guess_col = y
                        # if the space to the left was a hit
                        if p_board[x][y - 1] == "X":
                            # guess the space two to the left, if available
                            if y > 1:
                                if p_board[x][y - 2] != "X" and p_board[x][y - 2] != "M":
                                    if p_board[x][y - 2] != "O" or p_board[x][y + 1] != "O":
                                        c_guess_row = x + 1
                                        c_guess_col = y - 1
                            # if it is in column one
                            elif y == 1:
                                # guess the space to the right, if available
                                if p_board[x][y + 1] != "X" and p_board[x][y + 1] != "M" and p_board [x][y + 1] != "O":
                                    c_guess_row = x + 1
                                    c_guess_row = y + 2
                        # if the space to the right was a hit
                        if p_board[x][y + 1] == "X":
                            # guess the space two to the right, if available
                            if y < 8:
                                if p_board[x][y + 2] != "X" and p_board[x][y + 2] != "M":
                                    if p_board[x][y + 2] != "O" or p_board[x][y - 1] != "O":
                                        c_guess_row = x + 1
                                        c_guess_col = y + 3
                            # if it is in column nine
                            elif y == 9:
                                #guess the space to the left, if available
                                if p_board[x][y - 1] != "X" and p_board[x][y - 1] != "M" and p_board[x][y - 1] != "O":
                                    c_guess_row = x + 1
                                    c_guess_col = y
                        # if the space above was  a hit
                        if p_board[x - 1][y] == "X":
                            # guess the space two above, if available
                            if x > 1:
                                if p_board[x - 2][y] != "X" and p_board[x - 2][y] != "M":
                                    if p_board[x - 2][y] == "O" and p_board[x + 1][y] == "O":
                                        h = 0
                                    else:
                                        c_guess_row = x - 1
                                        c_guess_col = y + 1
                            elif x == 1:
                                if p_board[x + 1][y] != "X" and p_board[x + 1][y] != "M" and p_board[x + 1][y] != "O":
                                    c_guess_row = x + 2
                                    c_guess_col = y + 1
                                        
                        # if the space below was a hit
                        if p_board[x + 1][y] == "X":
                            # guess the space two below, if available
                            if x < 8:
                                if p_board[x + 2][y] != "X" and p_board[x + 2][y] != "M":
                                    if p_board[x + 2][y] == "O" and p_board[x - 1][y] == "O":
                                        h = 0
                                    else:
                                        c_guess_row = x + 3
                                        c_guess_col = y + 1
                            # if it is in row nine
                            elif x == 8:
                                if p_board[x - 1][y] != "X" and p_board[x - 1][y] != "M" and p_board[x - 1][y] != "O":
                                    c_guess_row = x
                                    c_guess_col = y + 1
                    # if it is on the UPPER edge
                    if x == 0 and y != 0 and y != 9:
                        # if the spaces around have not been hits, guess the space below
                        if p_board[x + 1][y] != "X" and p_board[x + 1][y] != "M"and p_board[x][y + 1] != "X" and p_board[x][y - 1] != "X":
                            c_guess_row = x + 2
                            c_guess_col = y + 1
                        # if the space below was a miss, and the others haven't been guessed
                        if p_board[x + 1][y] == "M"and p_board[x][y + 1] != "X" and p_board[x][y + 1] != "M" and p_board[x][y - 1] != "X":
                            # guess the space to the right
                            c_guess_row = x + 1
                            c_guess_col = y + 2
                        # if the spaces below, to the right were misses
                        if p_board[x + 1][y] == "M" and p_board[x][y + 1] == "M"and p_board[x][y - 1] != "M" and p_board[x][y - 1] != "X":
                            # guess the space to the left
                            c_guess_row = x + 1
                            c_guess_col = y
                        # if the space to the left was a hit
                        if p_board[x][y - 1] == "X":
                            # guess the space two to the left, if available
                            if y > 1:
                                if p_board[x][y - 2] != "X" and p_board[x][y - 2] != "M":
                                    if p_board[x][y - 2] != "O" or p_board[x][y + 1] != "O":
                                        c_guess_row = x + 1
                                        c_guess_col = y - 1
                            # if it is in column one
                            elif y == 1:
                                # guess the space to the right, if available
                                if p_board[x][y + 1] != "X" and p_board[x][y + 1] != "M" and p_board [x][y + 1] != "O":
                                    c_guess_row = x + 1
                                    c_guess_row = y + 2
                        # if the space to the right was a hit
                        if p_board[x][y + 1] == "X":
                            # guess the space two to the right, if available
                            if y < 8:
                                if p_board[x][y + 2] != "X" and p_board[x][y + 2] != "M":
                                    if p_board[x][y + 2] == "O" and p_board[x][y - 1] == "O":
                                        h = 0
                                    else:
                                        c_guess_row = x + 1
                                        c_guess_col = y + 3
                            # if it is in column nine
                            elif y == 9:
                                #guess the space to the left, if available
                                if p_board[x][y - 1] != "X" and p_board[x][y - 1] != "M" and p_board[x][y - 1] != "O":
                                    c_guess_row = x + 1
                                    c_guess_col = y
                                        
                        # if the space below was a hit
                        if p_board[x + 1][y] == "X":
                            # guess the space two below, if available
                            if x < 8:
                                if p_board[x + 2][y] != "X" and p_board[x + 2][y] != "M":
                                    if p_board[x + 2][y] == "O" and p_board[x - 1][y] == "O":
                                        h = 0
                                    else:
                                        c_guess_row = x + 3
                                        c_guess_col = y + 1










                    # if it is on the LEFT edge
                    if y == 0 and x != 0 and x != 9:
                        # if the spaces around have not been hits, guess the space below
                        if p_board[x + 1][y] != "X" and p_board[x + 1][y] != "M" and p_board[x - 1][y] != "X" and p_board[x][y + 1] != "X":
                            c_guess_row = x + 2
                            c_guess_col = y + 1
                        # if the space below was a miss, and the others haven't been guessed
                        if p_board[x + 1][y] == "M" and p_board[x - 1][y] != "X" and p_board[x][y + 1] != "X" and p_board[x][y + 1] != "M":
                            # guess the space to the right
                            c_guess_row = x + 1
                            c_guess_col = y + 2
                        # if the spaces below and to the right were misses
                        if p_board[x + 1][y] == "M" and p_board[x][y + 1] == "M" and p_board[x - 1][y] != "M" and p_board[x - 1][y] != "X":
                            # guess the space above
                            c_guess_row = x
                            c_guess_col = y + 1
                        # if the space to the right was a hit
                        if p_board[x][y + 1] == "X":
                            # guess the space two to the right, if available
                            if y < 8:
                                if p_board[x][y + 2] != "X" and p_board[x][y + 2] != "M":
                                    if p_board[x][y + 2] == "O" and p_board[x][y - 1] == "O":
                                        h = 0
                                    else:
                                        c_guess_row = x + 1
                                        c_guess_col = y + 3
                        # if the space above was  a hit
                        if p_board[x - 1][y] == "X":
                            # guess the space two above, if available
                            if x > 1:
                                if p_board[x - 2][y] != "X" and p_board[x - 2][y] != "M":
                                    if p_board[x - 2][y] == "O" and p_board[x + 1][y] == "O":
                                        h = 0
                                    else:
                                        c_guess_row = x - 1
                                        c_guess_col = y + 1
                                        
                        # if the space below was a hit
                        if p_board[x + 1][y] == "X":
                            # guess the space two below, if available
                            if x < 8:
                                if p_board[x + 2][y] != "X" and p_board[x + 2][y] != "M":
                                    if p_board[x + 2][y] == "O" and p_board[x - 1][y] == "O":
                                        h = 0
                                    else:
                                        c_guess_row = x + 3
                                        c_guess_col = y + 1










                # if it is on the LOWER edge
                if x == 9 and y != 0 and y != 9:
                        # if the space below was a miss, and the others haven't been guessed
                        if p_board[x - 1][y] != "X" and p_board[x][y + 1] != "X" and p_board[x][y + 1] != "M" and p_board[x][y - 1] != "X":
                            # guess the space to the right
                            c_guess_row = x + 1
                            c_guess_col = y + 2
                        # if the spaces below and to the right were misses
                        if p_board[x][y + 1] == "M" and p_board[x - 1][y] != "M" and p_board[x - 1][y] != "X" and p_board[x][y - 1] != "X":
                            # guess the space above
                            c_guess_row = x
                            c_guess_col = y + 1
                        # if the spaces below, to the right, and above were misses
                        if p_board[x][y + 1] == "M" and p_board[x - 1][y] == "M" and p_board[x][y - 1] != "M" and p_board[x][y - 1] != "X":
                            # guess the space to the left
                            c_guess_row = x + 1
                            c_guess_col = y
                        # if the space to the left was a hit
                        if p_board[x][y - 1] == "X":
                            # guess the space two to the left, if available
                            if y > 1:
                                if p_board[x][y - 2] != "X" and p_board[x][y - 2] != "M":
                                    if p_board[x][y - 2] != "O" or p_board[x][y + 1] != "O":
                                        c_guess_row = x + 1
                                        c_guess_col = y - 1
                            # if it is in column one
                            elif y == 1:
                                # guess the space to the right, if available
                                if p_board[x][y + 1] != "X" and p_board[x][y + 1] != "M" and p_board [x][y + 1] != "O":
                                    c_guess_row = x + 1
                                    c_guess_row = y + 2
                        # if the space to the right was a hit
                        if p_board[x][y + 1] == "X":
                            # guess the space two to the right, if available
                            if y < 8:
                                if p_board[x][y + 2] != "X" and p_board[x][y + 2] != "M":
                                    if p_board[x][y + 2] == "O" and p_board[x][y - 1] == "O":
                                        h = 0
                                    else:
                                        c_guess_row = x + 1
                                        c_guess_col = y + 3
                            # if it is in column nine
                            elif y == 9:
                                #guess the space to the left, if available
                                if p_board[x][y - 1] != "X" and p_board[x][y - 1] != "M" and p_board[x][y - 1] != "O":
                                    c_guess_row = x + 1
                                    c_guess_col = y
                        # if the space above was  a hit
                        if p_board[x - 1][y] == "X":
                            # guess the space two above, if available
                            if x > 1:
                                if p_board[x - 2][y] != "X" and p_board[x - 2][y] != "M":
                                    if p_board[x - 2][y] == "O" and p_board[x + 1][y] == "O":
                                        h = 0
                                    else:
                                        c_guess_row = x - 1
                                        c_guess_col = y + 1








                # if it is on the RIGHT edge
                if y == 9 and x != 0 and x != 9:
                    # if the spaces around have not been hits, guess the space below
                        if p_board[x + 1][y] != "X" and p_board[x + 1][y] != "M" and p_board[x - 1][y] != "X" and p_board[x][y - 1] != "X":
                            c_guess_row = x + 2
                            c_guess_col = y + 1
                        # if the spaces below and to the right were misses
                        if p_board[x + 1][y] == "M"and p_board[x - 1][y] != "M" and p_board[x - 1][y] != "X" and p_board[x][y - 1] != "X":
                            # guess the space above
                            c_guess_row = x
                            c_guess_col = y + 1
                        # if the spaces below, to the right, and above were misses
                        if p_board[x + 1][y] == "M" and p_board[x - 1][y] == "M" and p_board[x][y - 1] != "M" and p_board[x][y - 1] != "X":
                            # guess the space to the left
                            c_guess_row = x + 1
                            c_guess_col = y
                        # if the space to the left was a hit
                        if p_board[x][y - 1] == "X":
                            # guess the space two to the left, if available
                            if y > 1:
                                if p_board[x][y - 2] != "X" and p_board[x][y - 2] != "M":
                                    if p_board[x][y - 2] != "O" or p_board[x][y + 1] != "O":
                                        c_guess_row = x + 1
                                        c_guess_col = y - 1
                            
                       
                        # if the space above was  a hit
                        if p_board[x - 1][y] == "X":
                            # guess the space two above, if available
                            if x > 1:
                                if p_board[x - 2][y] != "X" and p_board[x - 2][y] != "M":
                                    if p_board[x - 2][y] == "O" and p_board[x + 1][y] == "O":
                                        h = 0
                                    else:
                                        c_guess_row = x - 1
                                        c_guess_col = y + 1
                                        
                        # if the space below was a hit
                        if p_board[x + 1][y] == "X":
                            # guess the space two below, if available
                            if x < 8:
                                if p_board[x + 2][y] != "X" and p_board[x + 2][y] != "M":
                                    if p_board[x + 2][y] == "O" and p_board[x - 1][y] == "O":
                                        h = 0
                                    else:
                                        c_guess_row = x + 3
                                        c_guess_col = y + 1
                                
              
        print "I guess (" + str(c_guess_row) + ", " + str(c_guess_col) + ")!" 
        for a in p_ship1_row:
            if a == c_guess_row:
                for b in p_ship1_col:
                    if b == c_guess_col:
                        print "I hit your aircraft carrier!"
                        p_board[c_guess_row - 1][c_guess_col - 1] = "X"
                        hom = 1
                        if len(p_ship1_row) > 1:
                            p_ship1_row.remove(c_guess_row)
                        elif len(p_ship1_col) > 1:
                            p_ship1_col.remove(c_guess_col)
                        if len(p_ship1_row) == 1 and len(p_ship1_col) == 1:
                            print "I sank your aircraft carrier!"
                            
        for a in p_ship2_row:
            if a == c_guess_row:
                for b in p_ship2_col:
                    if b == c_guess_col:
                        print "I hit your battleship!"
                        p_board[c_guess_row - 1][c_guess_col - 1] = "X"
                        hom = 2
                        if len(p_ship1_row) > 1:
                            p_ship2_row.remove(c_guess_row)
                        elif len(p_ship2_col) > 1:
                            p_ship2_col.remove(c_guess_col)
                        if len(p_ship2_row) == 1 and len(p_ship2_col) == 1:
                            print "I sank your batteship!"
                            
        for a in p_ship3_row:
            if a == c_guess_row:
                for b in p_ship3_col:
                    if b == c_guess_col:
                        print "I hit your submarine!" 
                        p_board[c_guess_row - 1][c_guess_col - 1] = "X"
                        hom = 3
                        if len(p_ship3_row) > 1:
                            p_ship3_row.remove(c_guess_row)
                        elif len(p_ship3_col) > 1:
                            p_ship3_col.remove(c_guess_col)
                        if len(p_ship3_row) == 1 and len(p_ship3_col) == 1:
                            print "I sank your submarine!"
        for a in p_ship4_row:
            if a == c_guess_row:
                for b in p_ship4_col:
                    if b == c_guess_col:
                        print "I hit your destroyer!"
                        p_board[c_guess_row - 1][c_guess_col - 1] = "X"
                        hom = 4
                        if len(p_ship4_row) > 1:
                            p_ship4_row.remove(c_guess_row)
                        elif len(p_ship4_col) > 1:
                            p_ship4_col.remove(c_guess_col)
                        if len(p_ship4_row) == 1 and len(p_ship4_col) == 1:
                            print "I sank your destroyer!"
        for a in p_ship5_row:
            if a == c_guess_row:
                for b in p_ship5_col:
                    if b == c_guess_col:
                        print "I hit your patrol boat!"
                        p_board[c_guess_row - 1][c_guess_col - 1] = "X"
                        hom = 5
                        if len(p_ship5_row) > 1:
                            p_ship5_row.remove(c_guess_row)
                        elif len(p_ship5_col) > 1:
                            p_ship5_col.remove(c_guess_col)
                        if len(p_ship5_row) == 1 and len(p_ship5_col) == 1:
                            print "I sank your patrol boat!"
        if hom == 0:
            print "Miss!"
            if p_board[c_guess_row - 1][c_guess_col - 1] != "X":
                p_board[c_guess_row - 1][c_guess_col - 1] = "M"
        print_board(p_board)
        print len(p_ship1_row)
        print len(p_ship1_col)
    rnd = 1
    p_score = 0
    c_score = 0
    while 1 < 2:
        print "Round " + str(rnd)
        p_guess()
        if len(p_ship1_row) == 1 and len(p_ship1_col) == 1:
            if len(p_ship2_row) == 1 and len(p_ship2_col) == 1:
                if len(p_ship3_row) == 1 and len(p_ship3_col) == 1:
                    if len(p_ship4_row) == 1 and len(p_ship4_col) == 1:
                        if len(p_ship5_row) == 1 and len(p_ship5_col) == 1:
                            print "Game over!"
                            print "I win!"
                            break
        if len(c_ship1_row) == 1 and len(c_ship1_col) == 1:
            if len(c_ship2_row) == 1 and len(c_ship2_col) == 1:
                if len(c_ship3_row) == 1 and len(c_ship3_col) == 1:
                    if len(c_ship4_row) == 1 and len(c_ship4_col) == 1:
                        if len(c_ship5_row) == 1 and len(c_ship5_col) == 1:
                            print "Game over!"
                            print "You win!"
                            break
        c_guess()
        rnd = rnd + 1
        if len(p_ship1_row) == 1 and len(p_ship1_col) == 1:
            if len(p_ship2_row) == 1 and len(p_ship2_col) == 1:
                if len(p_ship3_row) == 1 and len(p_ship3_col) == 1:
                    if len(p_ship4_row) == 1 and len(p_ship4_col) == 1:
                        if len(p_ship5_row) == 1 and len(p_ship5_col) == 1:
                            print "Game over!"
                            print "I win!"
                            break
        if len(c_ship1_row) == 1 and len(c_ship1_col) == 1:
            if len(c_ship2_row) == 1 and len(c_ship2_col) == 1:
                if len(c_ship3_row) == 1 and len(c_ship3_col) == 1:
                    if len(c_ship4_row) == 1 and len(c_ship4_col) == 1:
                        if len(c_ship5_row) == 1 and len(c_ship5_col) == 1:
                            print "Game over!"
                            print "You win!"
                            break
        
    print "Want to play again?"






    
                        
                        







                        
                       
