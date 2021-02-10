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

# Could be improved with lists of comprehension
def quantities_buy(coffee_type):
    global water, milk, beans, cups, money

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
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    coffee_type = int(input())
    quantities_buy(coffee_type)

def fill_action():
    global water, milk, beans, cups

    print("Write how many ml of water do you want to add:")
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

values_machine()
print("Write action (buy, fill, take):")
action = input()

if action == "take":
    take_action()
elif action == "fill":
    fill_action()
else:
    buy_action()

values_machine()

'''
def answer(coffees, w, m, b):
    water_coffees = w // water
    milk_coffees = m // milk
    beans_coffees = b // beans

    if coffees == min(water_coffees, milk_coffees, beans_coffees):
        print("Yes, I can make that amount of coffee")
    elif coffees > min(water_coffees, milk_coffees, beans_coffees):
        print(f"No, I can make only {min(water_coffees, milk_coffees, beans_coffees)} cups of coffee")
    else:
        print(f"Yes, I can make that amount of coffee (and even {min(water_coffees, milk_coffees, beans_coffees) - coffees} more than that)")

print("Write how many ml of water the coffee machine has:")
w = int(input())

print("Write how many ml of milk the coffee machine has:")
m = int(input())

print("Write how many grams of coffee beans the coffee machine has:")
b = int(input())

print("Write how many cups of coffee you will need:")
coffees = int(input())

answer(coffees, w, m, b)
'''