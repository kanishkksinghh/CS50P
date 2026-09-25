def main():
    amount_due = 50

    while amount_due > 0:
        print(f"Amount due: {amount_due}")
        coin = int(input("Insert Coin:"))

    if coin in[25, 10, 5]:
        amount_due -= coin

    change_owed: int = abs(amount_due)
    print(f"Changed owed:  {change_owed}")

if __name__ == "__main__":
    main()


