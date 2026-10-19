from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    s = input("Input: ")
    random.shuffle(fonts)
    figlet.setFont(font=fonts[0])
    print(figlet.renderText(s))

elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in fonts:
            s = input("Input: ")
            figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(s))
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid Usage")

else:
    sys.exit("Invalid usage")