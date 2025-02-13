import os
import time

import restaurant_module

name = input("What is the name of your restaurant? ")
os.system("cls")

restaurant = restaurant_module.Restaurant(name)

while True:
    print(f" {name.title()} ".center(30, "="))
    print("[1] -> Serve Customer\n[2] -> Get Results\n[0] -> Exit")
    selection = input("Select: ")

    if selection == "1":
        price = float(input("\nInput Customer's Bill: "))

        if restaurant.serve_customer(price):
            print("Customer Already Served!")
            time.sleep(1.5)
            os.system("cls")
        else:
            print("Invalid Price!")
            time.sleep(1.0)
            os.system("cls")

    elif selection == "2":
        restaurant.get_results()
        time.sleep(2.0)
        os.system("cls")

    elif selection == "0":
        break

    else:
        print("Invalid Option!")
        time.sleep(1.0)
        os.system("cls")

print(" Thank You For Using the Program! Have A Good Day! ".center(46, "="))
