#Vanity Plates
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    #rule 1 - length of plate between 2 and 6
    if not (2 <= len(s) <= 6):
        return False

    #rule 2 - only letters and numbers allowed.
    if not s.isalnum(): #.isalnum() returns True only if every character in the string is either a letter or a number — no spaces, no punctuation, no symbols.
        return False

    #rule 3 - must start with atleast 2 letters.
    if not s[0].isalpha() or not s[1].isalpha(): #.isalpha() checks if a single character is a letter (not a digit, not a symbol).
        return False

    #rule 4 - numbers must all be at the end, first one can't be 0.
    seen_digit = False
    for char in s:
        if char.isdigit():
            if not seen_digit and char == "0":
                return False
            seen_digit = True
        else:
            if seen_digit:
                return False

    return True

if __name__ == "__main__":
    main()


