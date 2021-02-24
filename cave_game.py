import shelve

cave = shelve.open('cave')

loc = 1
while True:
    available_exits = ", ".join(cave['venues'][loc]["exits"].keys())
    print(cave['venues'][loc]["desc"])

    if loc == 0:
        print("Thank you for playing this adventure game, maybe next time you can play again!")
        break

    else:
        all_exits = cave['venues'][loc]["exits"].copy()
        all_exits.update(cave['venues'][loc]["named_exits"])

    direction = input("The available exits are " + available_exits + " ").upper()
    print()

    if len(direction) > 1:
        words = direction.split()
        for word in words:
            if word in all_exits.keys():
                direction = word
            if word in cave['word_book']:
                direction = cave['word_book'][word]

    if direction in all_exits:
        loc = all_exits[direction]

    else:
        print("Sorry, you cannot exit in this direction / there is no such direction.")

cave.close()

