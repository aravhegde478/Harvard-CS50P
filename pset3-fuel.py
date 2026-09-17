#fuel
while True:
    try:
        x = input("Enter a fraction: ")
        m, n = x.split("/")
        m = int(m)
        n = int(n)
        if m > n:
            raise ValueError
        z = round((m / n) * 100)
    except ValueError:
        print("You have not entered integers, or the fraction is invalid")
    except ZeroDivisionError:
        print("You cannot divide by zero")
    else:
        if z <= 1:
            print("E")
        elif z >= 99:
            print("F")
        else:
            print(f"{z}%")
        break