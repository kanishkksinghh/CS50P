import inflect

def main():
    p = inflect.engine()
    names = []

    while True:
        try:
            name = input("Name: ").strip()
            if name:
                names.append(name)
        except EOFError:
            print()
            break

    formatted_names = p.join(names)
    print(f"Adieu, adieu, to {formatted_names}")

if __name__ == "__main__":
    main()

