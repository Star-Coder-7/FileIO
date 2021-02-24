import shelve

with shelve.open("bike2") as bike:
    # bike["make"] = "Toyota"
    # bike["model"] = "100 dream"
    # bike["color"] = "blue and purple"
    # bike["engine_size"] = 300

    del bike["engine_size"]

    for key in bike:
        print(key)

    print("=" * 50)

    print(bike["engine_size"])
    # print(bike["engin_size"])
    print(bike["color"])



















