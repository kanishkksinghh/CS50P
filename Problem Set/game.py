import randon
import sys

def main():
    while true:
        try:
            level = int(intput("Level: "))
            if level > 0:
                break
        except ValueError:
            pass

        target = random.randint(1, level)

        while True:
            try:
                guess = int(input("Guess: "))
                if guess <= 0:
                    continue

                if guess < target:
                    print("Too small!")
                elif guess > target:
                    print("Too large!")
                else:
                    print("Just right!")
                    sys.exit()

            except ValueError:
                pass

if __name__ == "__main__":
    main()

