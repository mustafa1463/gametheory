print("="*40)
print("Welcome to the Game Theory Application of Mustafa for Static Games of Complete Information!")
print("We can, for now, only solve 2x2 matrice games with strictly eliminated strategies. ")
print("="*40)
while True:

    C = input("The first strategy of players: ")
    D = input("The second strategy of player: ")
    print("Now you will enter the pay-offs;")

    e = int(input("Player 1's outcome for {},{}: ".format(C, C)))
    g = int(input("Player 1's outcome for {},{}: ".format(C, D)))
    f = int(input("Player 1's outcome for {},{}: ".format(D, C)))
    h = int(input("Player 1's outcome for {},{}: ".format(D, D)))

    x = int(input("Player 2's outcome for {},{}: ".format(C, C)))
    y = int(input("Player 2's outcome for {},{}: ".format(D, C)))
    z = int(input("Player 2's outcome for {},{}: ".format(C, D)))
    m = int(input("Player 2's outcome for {},{}: ".format(D, D)))

    if e > f and g > h:

        if x > z:
            print("Player 1 chooses {}".format(C))
            print("Player 2 chooses {}".format(C))
            print("The Iterated elimination outcome of the game is {},{}".format(C, C))
        elif x < z:
            print("Player 1 chooses {}".format(C))
            print("Player 2 chooses {}".format(D))
            print("The Iterated elimination outcome of the game is {},{}".format(C, D))

    elif e < f and g < h:

        if y > m:
            print("Player 1 chooses {}".format(D))
            print("Player 2 chooses {}".format(C))
            print("The Iterated elimination outcome of the game is {}".format(D, C))

        elif y < m:
            print("Player 1 chooses {}".format(D))
            print("Player 2 chooses {}".format(D))
            print("The Iterated elimination outcome of the game is {},{}".format(D, D))

    elif x > z and y > m:

        if e > f:
            print("Player 2 chooses {}".format(C))
            print("Player 1 chooses {}".format(C))
            print("The Iterated elimination outcome of the game is {},{}".format(C, C))

        elif e < f:
            print("Player 2 chooses {}".format(C))
            print("Player 1 chooses {}".format(D))
            print("The Iterated elimination outcome of the game is {},{}".format(D, C))

        else:
            print("Player 1 is indifferent between {} or {}".format(C, D))
            print("Hence, the iterated elimination suggests that the outcome is either {},{} or {},{}".format(C, C, D, C))

    elif x < z and y < m:

        if g > h:
            print("Player 2 chooses {}".format(D))
            print("Player 1 chooses {}".format(C))
            print("The iterated elimination suggests that the outcome is {},{}".format(C, D))

        if g < h:
            print("Player 2 chooses {}".format(D))
            print("Player 1 chooses {}".format(D))
            print("The iterated elimination suggests that the outcome is {},{}".format(D, D))

        else:
            print("Player 2 chooses {}".format(D))
            print("The iterated elimination suggests that the outcome is indifferent between {},{}".format(C, D))
            print("Hence, the outcome is either {},{} or {},{}".format(C, D, D, D))

    elif x == z and y == m:

        if e == f and g == h:
            print("No solution! Players are indifferent between any choice!")

        elif e > f and g > h:
            print("Player 1 chooses {}".format(C))
            print("However, since Player 2 is indifferent between {} and {}, no iterated outcome".format(C, D))

        elif e < f and g < h:
            print("Player 1 chooses {}".format(D))
            print("However, since Player 2 is indifferent between {} and {}, no iterated outcome".format(C, D))

    elif e == f and g == h:
        if x == z and y == m:
            print("No solution! Players are indifferent between any choice!")

        elif x > z and y > m:
            print("Player 2 chooses {}".format(C))
            print("However, since Player 1 is indifferent between {} and {}, no iterated outcome".format(C, D))

        elif x < z and y < m:
            print("Player 2 chooses {}".format(D))
            print("However, since Player 1 is indifferent between {} and {}, no iterated outcome".format(C, D))

    elif e == f and g == h:
        print("No solution in Iterated Elimination")

    else:
        print("No solution in Iterated Elimination!")
