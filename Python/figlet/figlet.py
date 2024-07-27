from pyfiglet import Figlet
import sys

figlet = Figlet()

#Checking if the user writes 0 or 2 command line arguments#
if len(sys.argv) not in (1, 3):
    print("Invalid Usage.")
    sys.exit(1)
#If the command line arguments are 2 but the first is not --font or -f, returns an error message.#
elif len(sys.argv) == 3 and (sys.argv[1] != '--font' and sys.argv[1] != '-f'):
    print("Invalid Usage.")
    sys.exit(1)
elif len(sys.argv) == 3:
    f = sys.argv[2]
    #Setting the font chosen by the user.
    figlet.setFont(font=f)

s = input("Enter a Text: ")
print(figlet.renderText(s))
