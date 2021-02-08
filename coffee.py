# Making coffee

def quantities(coffees):
    print(f"{coffees * 200} ml of water")
    print(f"{coffees * 50} ml of milk")
    print(f"{coffees * 15} g of coffee beans")

print("Write how many cups of coffee you will need:")
coffees = int(input())

print(f"For {coffees} cups of coffee you will need:")
quantities(coffees)