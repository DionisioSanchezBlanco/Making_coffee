# Making coffee

# Values by default
water, milk, beans, money, cups = 400, 540, 120, 550, 9

# Values: [water, milk, beans, money]
espresso = [250, 0, 16, 4]
latte = [350, 75, 20, 7]
capuccino = [200, 100, 12, 6]

def values_machine():
    print(f"\nThe coffee machine has:")
    print(f"{water} of water")
    print(f"{milk} of milk")
    print(f"{beans} of coffee beans")
    print(f"{cups} of disposable cups")
    print(f"{money} of money")

def check_resources(coffee_type):
    if coffee_type == 2:
        if latte[0] > water:
            print("Sorry, not enough water!")
        elif latte[2] > beans:
            print("Sorry, not enough cofee beans!")
        elif latte[1] > milk:
            print("Sorry, not enough milk!")
        else:
            print("I have enough resources, making you a coffee!")
            return 1

    if coffee_type == 3:
        if capuccino[0] > water:
            print("Sorry, not enough water!")
        elif capuccino[2] > beans:
            print("Sorry, not enough cofee beans!")
        elif capuccino[1] > milk:
            print("Sorry, not enough milk!")
        else:
            print("I have enough resources, making you a coffee!")
            return 1

    if coffee_type == 1:
        if espresso[0] > water:
            print("Sorry, not enough water!")
        elif espresso[2] > beans:
            print("Sorry, not enough cofee beans!")
        else:
            print("I have enough resources, making you a coffee!")
            return 1


# Could be improved with lists of comprehension
def quantities_buy(coffee_type):
    global water, milk, beans, cups, money

    if check_resources(coffee_type) != True:
        pass
    else:
        if coffee_type == 1:
            water -= espresso[0]
            beans -= espresso[2]
            money += espresso[3]
        elif coffee_type == 2:
            water -= latte[0]
            milk -= latte[1]
            beans -= latte[2]
            money += latte[3]
        else:
            water -= capuccino[0]
            milk -= capuccino[1]
            beans -= capuccino[2]
            money += capuccino[3]

        cups -= 1


def buy_action():
    print("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    coffee_type = input()
    if coffee_type != "back":
        quantities_buy(int(coffee_type))

def fill_action():
    global water, milk, beans, cups

    print("\nWrite how many ml of water do you want to add:")
    water += int(input())
    print("Write how many ml of milk do you want to add:")
    milk += int(input())
    print("Write how many grams of coffee beans do you want to add:")
    beans += int(input())
    print("Write how many disposable cups of coffee do you want to add:")
    cups += int(input())

def take_action():
    global money
    print(f"I gave you ${money}")
    money = 0

print("\nWrite action (buy, fill, take, remaining, exit):")
action = input()

while action != "exit":

    if action != "exit":
        if action == "take":
            take_action()
        elif action == "fill":
            fill_action()
        elif action == "buy":
            buy_action()
        else:
            values_machine()
    else:
        break
    
    action = None
    print("\nWrite action (buy, fill, take, remaining, exit):")
    action = input()
