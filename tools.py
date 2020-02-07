import re
import random as rand


def roll(s, mod=0):
    if re.match(re.compile("^[0-9]+d[0-9]+$"), s.lower()):
        p = s.lower().split("d")
        rolls = [rand.randint(1, int(p[1])) for i in range(int(p[0]))]
    elif re.match(re.compile("^[0-9]+$"), s):
        rolls = [int(s)]
    else:
        print("You fucked up")
        rolls = [0]
    return rolls, sum(rolls) + mod


def print_menu(l):
    print("\n\n" + "*" * 20)
    for i in range(len(l)):
        print("[{}] {}".format(i + 1, l[i]))

    print("*" * 20)
