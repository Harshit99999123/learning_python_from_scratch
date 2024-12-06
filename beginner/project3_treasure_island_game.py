print("Welcome to the Treasure Island.\nYour mission is to find the treasure.")
direction = input("left or right? ")
if direction != "left" and direction != "right":
    print(f"Invalid direction entered: {direction}\nGame over")
elif direction == "right":
    print("Game over")
else:
    activity = input("swim or wait? ")
    if activity != "swim" and activity != "wait":
        print(f"Activity {activity} not supported.\nGame over")
    elif activity == "swim":
        print("Game over")
    else:
        door = input("Which door? red, yellow or blue ")
        if door == "red" or door == "yellow":
            print("Game over")
        elif door == "blue":
            print("You win!")
        else:
            print(f"Invalid door {door}.\nGame over")

