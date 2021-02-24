with open("sample.txt", 'w') as multiplication_tables:
    for i in range(2, 13):
        for x in range(1, 13):
            print(f"{i} times {x} is {i*x}", file=multiplication_tables)
    print("=" * 50, file=multiplication_tables)
