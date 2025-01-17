####################################################
# CS 31, Prof. Muldrow
# Name: Wolf Tripp
# Assignment: Project 2
# Due Date: 11/18
####################################################

def main():
    numorders = 0
    while numorders <= 0:
        try:
            numorders = int(input("Enter how many orders you wish to make: "))
        except ValueError:
            print() # Console Readability
            print("This isnt a valid input try again")
            print() # Console Readability
    print('----------Processing Order #1----------')
    write_order()
    if numorders > 1:
        append_order(numorders)
    display_to_console()

def display_to_console():
    with open('order.txt', 'r') as orders:
        orderstart = orders.readline().rstrip('\n')
        while orderstart != '':
            sandwiches = orders.readline().rstrip('\n')
            sideorder = orders.readline().rstrip('\n')
            drink = orders.readline().rstrip('\n')
            divide = orders.readline().rstrip('\n')
            subtotal = orders.readline().rstrip('\n')
            tax = orders.readline().rstrip('\n')
            total = orders.readline().rstrip('\n')

            print(
                f'{orderstart}\n'
                f"{sandwiches}\n"
                f"{sideorder}\n"
                f"{drink}\n"
                f"{divide}\n"
                f"{subtotal}\n"
                f"{tax}\n"
                f"{total}\n"
            )
            orderstart = orders.readline().rstrip('\n')

def write_order():
    sandwiches, price1 = process_sandwichs()
    sideorders, price2 = process_side_orders()
    drink, drinksize, price3 = process_drinks()
    subtotal = price3 + price2 + price1
    drinkAndSize = str(drink) + " " + str(drinksize)
    tax = .08 * subtotal
    total = subtotal + tax
    if drinksize == 0:
        with open('order.txt', 'w') as order:
            order.write(f"~~~~~~~******* Total for Order #1 *******~~~~~~~\n")
            order.write(f"{sandwiches:24}${price1:.2f}\n")
            order.write(f"{sideorders:24}${price2:.2f}\n")
            order.write(f"{drink:24}${price3:.2f}\n")
            order.write(f"-----------------------------------\n")
            order.write(f"{"Subtotal:":24}${subtotal:.2f}\n")
            order.write(f"{"Tax:":24}${tax:.2f}\n")
            order.write(f"{"Total:":24}${total:.2f}\n")
    else:
        with open('order.txt', 'w') as order:
            order.write(f"~~~~~~~******* Total for Order #1 *******~~~~~~~\n")
            order.write(f"{sandwiches:24}${price1:.2f}\n")
            order.write(f"{sideorders:24}${price2:.2f}\n")
            order.write(f"{drinkAndSize:24}${price3:.2f}\n")
            order.write(f"-----------------------------------\n")
            order.write(f"{"Subtotal:":24}${subtotal:.2f}\n")
            order.write(f"{"Tax:":24}${tax:.2f}\n")
            order.write(f"{"Total:":24}${total:.2f}\n")

def append_order(numorders):
    for x in range(2, numorders + 1):
        print(f"----------Processing Order #{x}----------")
        sandwiches, price1 = process_sandwichs()
        sideorders, price2 = process_side_orders()
        drink, drinksize, price3 = process_drinks()
        subtotal = price3 + price2 + price1
        drinkAndSize = str(drink) + " " + str(drinksize)
        tax = .08 * subtotal
        total = subtotal + tax
        if drinksize == 0:
            with open('order.txt', 'a') as order:
                order.write(f"~~~~~~~******* Total for Order #{x} *******~~~~~~~\n")
                order.write(f"{sandwiches:24}${price1:.2f}\n")
                order.write(f"{sideorders:24}${price2:.2f}\n")
                order.write(f"{drink:24}${price3:.2f}\n")
                order.write(f"-----------------------------------\n")
                order.write(f"{"Subtotal:":24}${subtotal:.2f}\n")
                order.write(f"{"Tax:":24}${tax:.2f}\n")
                order.write(f"{"Total:":24}${total:.2f}\n")
        else:
            with open('order.txt', 'a') as order:
                order.write(f"~~~~~~~******* Total for Order #{x} *******~~~~~~~\n")
                order.write(f"{sandwiches:24}${price1:.2f}\n")
                order.write(f"{sideorders:24}${price2:.2f}\n")
                order.write(f"{drinkAndSize:24}${price3:.2f}\n")
                order.write(f"-----------------------------------\n")
                order.write(f"{"Subtotal:":24}${subtotal:.2f}\n")
                order.write(f"{"Tax:":24}${tax:.2f}\n")
                order.write(f"{"Total:":24}${total:.2f}\n")

def process_sandwichs():
    sandwich = 0
    # print() # Console Readability
    while sandwich <= 0 or sandwich > 4:
        try:
            sandwich = int(input(
                "What kind of sandwich you want?\n"
                "Enter 1 for a Hamburger\n"
                "Enter 2 for a Cheeseburger\n"
                "Enter 3 for a Chicken Sandwich\n"
                "Enter 4 for no sandwich\n"
            ))
        except ValueError:
            print() # Console Readability
            print("This isnt a valid input try again")
            print() # Console Readability
        if sandwich > 4 or sandwich <= 0:
            print() # Console Readability
            print("This isnt a valid input try again")
            print() # Console Readability
    match sandwich:
        case 1:
            sandwich = "Hamburger"
            price = 2.75
        case 2:
            sandwich = "Cheeseburger"
            price = 3.25
        case 3:
            sandwich = "Chicken Sandwich"
            price = 2.50
        case _:
            sandwich = 'No Sandwich Selected'
            price = 0.00
    return sandwich, price

def process_side_orders():
    print() # Console Readability
    sideorder = 0
    while sideorder <= 0 or sideorder > 4:
        try:
            sideorder = int(input(
                "What kind of side order you want?\n"
                "Enter 1 for French Fries\n"
                "Enter 2 for Onion Rings\n"
                "Enter 3 for a Salad\n"
                "Enter 4 for no side\n"
            ))
        except ValueError:
            print() # Console Readability
            print("This isnt a valid input try again")
            print() # Console Readability
        if sideorder > 4 or sideorder <= 0:
            print() # Console Readability
            print("This isnt a valid input try again")
            print() # Console Readability
    match sideorder:
        case 1:
            sideorder = "French Fries"
            price = 2.25
        case 2:
            sideorder = "Onion Rings"
            price = 1.75
        case 3:
            sideorder = "Salad"
            price = 1.50
        case _:
            sideorder = 'No Side Selected'
            price = 0.00
    return sideorder, price

def process_drinks():
    print() # Console Readability
    drink = 0
    price = 0
    drinksize = 0
    while drink <= 0 or drink > 4:
        try:
            drink = int(input(
            "What kind of drink you want?\n"
            "Enter 1 for Coke\n"
            "Enter 2 for Sprite\n"
            "Enter 3 for Lemonaide\n"
            "Enter 4 for a Water Cup\n"
            ))
        except ValueError:
            print() # Console Readability
            print("This isnt a valid input try again")
            print() # Console Readability
        if drink > 4 or drink <= 0:
            print() # Console Readability
            print("This isnt a valid input try again")
            print() # Console Readability

    match drink:
        case 1:
            drink = "Coke"
        case 2:
            drink = "Sprite"
        case 3:
            drink = "Lemonaide"
        case 4:
            drink = "Water Cup"
    if drink != "Water Cup":
        while drinksize <= 0 or drinksize > 3:
            try:
                drinksize = int(input(
                    "What size do you want?\n"
                    "Enter 1 for small\n"
                    "Enter 2 for medium\n"
                    "Enter 3 for large\n"
                ))
                print() #Console Readability
            except ValueError:
                print() # Console Readability
                print("This isnt a valid input try again")
                print() # Console Readability
            if drinksize > 3 or drinksize <= 0:
                print() # Console Readability
                print("This isnt a valid input try again")
                print() # Console Readability
        match drinksize:
            case 1:
                drinksize = "Small"
                price = 1.50
            case 2:
                drinksize = "Medium"
                price = 2.25
            case 3:
                drinksize = "Large"
                price = 2.75
    return drink, drinksize, price

main()