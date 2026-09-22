list = {}

while True:
    try:
        item = input("Enter an item: ").upper()
        if item not in list:
            list[item] = 1
        else:
            list[item] += 1
    except (EOFError, KeyError):
        break

for key in sorted(list):
    print (list[key], key)