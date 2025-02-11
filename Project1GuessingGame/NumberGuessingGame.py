import random

random_number = random.randint(1, 100)

#print(random_number)

game_count = 1

while True:
    try:
        my_number = int(input("Please enter a number between 1 and 100."))

        if my_number > random_number:
            print("Down")
        elif my_number < random_number:
            print("Up")
        elif my_number == random_number:
            print(f"Congratulations! You got it in {game_count} attempts!")
            break
    
        game_count = game_count + 1

    except:
        print("An error has occurred. Please enter a number.")
