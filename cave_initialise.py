import shelve

cave = shelve.open('cave')

cave['venues'] = {0: {"desc": "You are now sitting in front of a screen learning Python",
                      "exits": {},
                      "named_exits": {}},
                  1: {"desc": "You are now standing at the end of a road before a small brick building",
                      "exits": {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
                      "named_exits": {"2": 2, "3": 3, "5": 5, "4": 4, "0": 0}},
                  2: {"desc": "You are now at the top of a hill",
                      "exits": {"N": 5, "Q": 0},
                      "named_exits": {"5": 5, "0": 0}},
                  3: {"desc": "You are now inside a building, a well house for a small stream",
                      "exits": {"W": 1, "Q": 0},
                      "named_exits": {"1": 1, "0": 0}},
                  4: {"desc": "You are now in a valley beside a stream",
                      "exits": {"N": 1, "W": 2, "Q": 0},
                      "named_exits": {"1": 1, "2": 2, "0": 0}},
                  5: {"desc": "You are now in a forest",
                      "exits": {"W": 2, "S": 1, "Q": 0},
                      "named_exits": {"2": 2, "1": 1, "0": 0}}
                  }

cave['word_book'] = {"QUIT":     "Q",
                     "NORTH":    "N",
                     "SOUTH":    "S",
                     "EAST":     "E",
                     "WEST":     "W",
                     "ROAD":     "1",
                     "HILL":     "2",
                     "BUILDING": "3",
                     "VALLEY":   "4",
                     "FOREST":   "5".upper()}

cave.close()
