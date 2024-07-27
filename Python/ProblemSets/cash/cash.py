from cs50 import get_float


def main():
    cents = get_cents()

    # Calculate the number of quarters to give the customer
    quarters = calculate_quarters(cents)
    cents = cents - (quarters * 25)

    # Calculate the number of dimes to give the customer
    dimes = calculate_dimes(cents)
    cents = cents - (dimes * 10)

    # Calculate the number of nickels to give the customer
    nickels = calculate_nickels(cents)
    cents = cents - (nickels * 5)

    # Calculate the number of pennies to give the customer
    pennies = calculate_pennies(cents)
    cents = cents - (pennies * 1)

    # Sum coins
    total_coins = quarters + dimes + nickels + pennies
    print(total_coins)


def get_cents():
    while True:
        remaining = get_float("Change Owed: ")
        if remaining > 0:
            cents = remaining * 100
            return cents


def calculate_quarters(cents):
    quarter = 0
    while (cents >= 25):
        cents = cents - 25
        quarter += 1
    return quarter


def calculate_dimes(cents):
    dime = 0
    while (cents >= 10):
        cents = cents - 10
        dime += 1
    return dime


def calculate_nickels(cents):
    nickel = 0
    while (cents >= 5):
        cents = cents - 5
        nickel += 1
    return nickel


def calculate_pennies(cents):
    penny = 0
    while (cents >= 1):
        cents = cents - 1
        penny += 1
    return penny


main()
