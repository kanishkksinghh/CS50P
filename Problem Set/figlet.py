import random
import sys
from pyfiglet import Figlet


def main():
    figlet = Figlet()
    available_fonts = figlet.getFonts()

    # Determine font choice based on command-line arguments
    if len(sys.argv) == 1:
        font = random.choice(available_fonts)
    elif len(sys.argv) == 3:
        if sys.argv[1] not in ["-f", "--font"]:
            sys.exit("Invalid usage")
        if sys.argv[2] not in available_fonts:
            sys.exit("Invalid usage")
        font = sys.argv[2]
    else:
        sys.exit("Invalid usage")

    # Set chosen font
    figlet.setFont(font=font)

    # Prompt user for text
    text = input("Input: ")

    # Output ASCII art
    print("Output:")
    print(figlet.renderText(text))


if __name__ == "__main__":
    main()
