import tools
import json

try:
    with open("custom_dice.json", "r") as file:
        customs = json.load(file)
except FileNotFoundError:
    with open("custom_dice.json", "w+") as file:
        file.write("{}")
        print("File created")
    customs = dict()


def main():
    while True:
        menu()


def menu():
    options = {"Roll dice": roll, "Custom Dice": custom}

    print("\n\n")
    i = 1
    print("*" * 20)
    for k in options:
        print("[{}] {}".format(i, k))
        i += 1
    print("*" * 20)
    list(options.values())[int(input("Choice: "))-1]()


def roll(dice=None):
    if dice is not None:
        q = True
    else:
        q = False

    while True:
        if dice is None:
            dice = input("Dice: ")
        if dice.lower() == "q":
            return

        dice_set = dice.split(";")

        r = range(len(dice_set))

        for d in r:
            dice = dice_set[d]
            print("[{}]:".format(dice))
            dice_mult = dice.split("*")
            multi = 1
            if len(dice_mult) > 1:
                multi = int(dice_mult[1])
            dice = dice_mult[0]
            dice_split = dice.split("+")
            for i in range(multi):
                if len(dice_split) > 1:
                    result = tools.roll(dice_split[0], int(dice_split[1]))
                else:
                    result = tools.roll(dice)
                print("\tRoll {}: {}".format(i+1, result))
            print("")

        if q:
            return
        dice = None


def custom():
    while True:
        m = ["New custom roll"] + list(customs.keys()) + ["Delete custom roll"]

        print("\n\n" + "*" * 20)
        for i in range(len(m)):
            print("[{}] {}".format(i+1, m[i]))

        print("*" * 20)

        choice = input("Choice: ")
        if choice.lower() == "q":
            return
        else:
            choice = int(choice) - 1

        if choice == 0:
            name = input("Name dice roll: ")
            r = input("Input custom roll: ")
            customs[name] = r
            with open("custom_dice.json", "w+") as customs_file:
                json.dump(customs, customs_file)
        elif choice == len(m) - 1:
            tools.print_menu(list(customs.keys()))
            ch = int(input("Choice: ")) - 1
            del customs[list(customs.keys())[ch]]
            with open("custom_dice.json", "w+") as customs_file:
                json.dump(customs, customs_file)
        else:
            roll(customs[m[choice]])


main()
