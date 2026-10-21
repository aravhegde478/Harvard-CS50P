import inflect

p = inflect.engine()
list_of_names = []

while True:
    try:
        names = input("Enter name: ")
        list_of_names.append(names)
    except EOFError:
        break

formatted_list = p.join(list_of_names)
print ("Adieu, adieu, to", formatted_list)