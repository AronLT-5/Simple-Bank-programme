from time import sleep


def show_balance(balance):
    print(f"Your balance is: £{balance:.2f}")
    sleep(2)

def deposit():
    Amount = float(input("Enter an amount to be Deposited:"))

    if Amount < 0:
        print(f"{Amount} is not a valid input")
        sleep(2)
        return 0
    else:
        sleep(2)
        return Amount

def withdraw(balance):
    Amount = float(input("Enter an amount to Withdraw:"))

    if Amount > balance:
        print(f"Unable to Withdraw: {Amount} due to insufficient funds")
        sleep(2)
        return 0
    elif Amount < 0:
        print(f"{Amount} is not a valid input")
        sleep(2)
        return 0
    else:
        sleep(2)
        return Amount


def main():
    balance = 0

    is_running = True

    while is_running:
        print("------------------------------------------------------------------------------------------------")
        print("Personal Banking programme")

        print("Press 1: Show Balance")
        print("Press 2: Deposit")
        print("Press 3: Withdraw")
        print("Press 4: Exit")

        Choice = input("Make Your selection")

        if Choice == "1":
            show_balance(balance)

        elif Choice == "2":
           balance += deposit()
           show_balance(balance)


        elif Choice == "3":
            balance -= withdraw(balance)
            show_balance(balance)

        elif Choice == "4":
            is_running = False

        else:
            print(f"{Choice} is not a valid response")
            sleep(2)


    print("Thank you! Have a Nice Day")


if __name__ == '__main__':
    main()





