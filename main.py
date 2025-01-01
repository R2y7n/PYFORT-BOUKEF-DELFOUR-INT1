from math import *
import random
from utility_functions import *
from math_challenges import *
from logical_challenges import *
from pere_fouras_challenge import *
from final_challenge import *
from chance_challenges import *


if __name__ == "__main__":
    introduction()

    begin = input("enter 'start' to play : ")
    while begin != "start":
        begin = input("enter 'start' to play :")

    if begin == "start":
        n = int(input("enter the number of player : "))

        while n < 1 or n > 3:
            n = int(input("enter the number of player : "))
        team=compose_equip(n)

        keys_cpt=0
        while keys_cpt < 3:
            choice_of_challenge=challenges_menu()
            print(f'Selected challenge: {choice_of_challenge}')
            player_chosen=chose_player(team)
            print (f'The selected player is {player_chosen['name']}')
            if choice_of_challenge=="Mathematics challenge":
                win=math_challenge()
            elif choice_of_challenge=="Chance challenge":
                win=chance_challenge()
            elif choice_of_challenge=="Logic challenge":
                game_selected=random.choice(["The game of Nim","Tic-Tac-Toe","Battleship"])
                print(f"You are going to play a duel against the master of time at {game_selected}")
                if game_selected=="The game of Nim":
                    win=nim_game()
                if game_selected=="Tic-Tac-Toe":
                    win=tictactoe_game()
                if game_selected=="Battleship":
                    print("not added yet")
            elif choice_of_challenge=="Père Fouras'riddle":
                 win=pere_fouras_riddles()
            if win:
                player_chosen['keys_won'] = player_chosen['keys_won'] + 1
                keys_cpt+=1
            print(f"Keys collected:{keys_cpt}")
            if keys_cpt<3:
                print("You still have to collect",3-keys_cpt,"keys")

        print("Congratulations! You will now have to find the code word")

        found_code_word=treasure_room()
        if found_code_word:
            print("You win!")
        else:
            print("You lose!")



