from math import *
from utility_functions import *


if __name__ == "__main__":
    introduction()

    begin = input("enter start to play a game : ")

    if begin == "start":
        n = int(input("enter the number of player : "))

        while n < 1 or n > 3:
            n = int(input("enter the number of player : "))
        compose_equip(n)
    while begin != "start":
        begin = input("enter start to play a game :")
