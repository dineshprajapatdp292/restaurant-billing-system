menu = {
    1: ("Pizza", 200),
    2: ("Burger", 120),
    3: ("Pasta", 150),
    4: ("Coffee", 80)
}


cart = []
grand_total = 0

while True:

    print("\n------ MENU ------")

    for key, value in menu.items():
        print(key, ".", value[0], "=", value[1])

    choice = int(input("Enter item number: "))

    if choice not in menu:
        print("Invalid Choice")
        continue

    quantity = int(input("Enter quantity: "))

    item_name = menu[choice][0]
    price = menu[choice][1]

    total = price * quantity

    grand_total += total

    cart.append((item_name, quantity, total))

    more = input("Do you want another item? (yes/no): ")

    if more.lower() != "yes":
        break

print("\n------ FINAL BILL ------")

for item in cart:
    print(item[0], "x", item[1], "=", item[2])
print(cart)
print("------------------------")
print("Grand Total =", grand_total)