def main():
    account_one = input()
    account_two = input()
    amount = input()
    amount_one, amount_two = transaction(
        account_one=int(account_one), account_two=int(account_two), amount=int(amount)
    )
    print(amount_one, amount_two)


def transaction(account_one, account_two, amount):
    if amount > account_one:
        account_two += account_one
        account_one = 0
    else:
        account_one -= amount
        account_two += amount
    return account_one, account_two


if __name__ == "__main__":
    main()
