# Making coffee
water, milk, beans = 200, 50, 15

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