import shelve

# with shelve.open('ShelfTest') as fruit:
fruit = shelve.open('ShelfTest')
# fruit['orange'] = "a sweet, orange, citrus fruit."
# fruit['apple'] = "good for making cider."
# fruit['lemon'] = "a sour, yellow, citrus fruit."
# fruit['grape'] = "s small, sweet fruit growing on bunches."
# fruit['lime'] = "a sour, green, citrus fruit."

# print(fruit["lemon"])
# print(fruit["grape"])
#
# fruit["lime"] = "great with tequila"
#
# for food in fruit:
#     print(food + ": " + fruit[food])

# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit".casefold() or dict_key == "stop".casefold():
#         print("Aright, the program has been terminated")
#         break
#
#     if dict_key.casefold() in fruit:
#         description = fruit[dict_key]
#         print(description)
#     else:
#         print(dict_key + " isn't defined so it's invalid")

# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
#
# for f in ordered_keys:
#     print(f + "- " + fruit[f])

for v in fruit.values():
    print(v)

print(fruit.values())

for f in fruit.items():
    print(f)

print(fruit.items())

fruit.close()

















