import os

list_name = "ShoppingList.txt"

while True:
    print(" Grocery Shopping List ".center(45, "="))

    item_amount = int(input("\nEnter the number of items you want to add to your list: "))
    shopping_list = dict()

    for item in range(item_amount):
        item_name = input(f"\nEnter the name of Item #{item + 1}: ").capitalize()
        item_number = input(f"Enter amount of {item_name.lower()}: ")
        shopping_list[item_name] = item_number

    os.system("cls")

    print("Grocery Shopping List was successfully created! Confirm:\n")

    for item, quantity in shopping_list.items():
        print(f"Item: {item.capitalize()} -> Quantity: {quantity}")

    select = input("\n[1] -> Save List\n[0] -> Exit\n[Any Other Button] -> Create New List\nSelect: ")

    if select == "1":
        with open(list_name, "a", encoding="utf-8") as list:
            for item, quantity in shopping_list.items():
                list.write(f"Item: {item.capitalize()} -> Quantity: {quantity}\n")

        print("\nList Saved Succesfully! Confirm in 'ShoppingList.txt' !\n")
        break
            
    elif select == "0":
        break

    else:
        os.system("cls")

print(" Thank You For Using Our Program! Have a Good Day! ".center(47, "="))