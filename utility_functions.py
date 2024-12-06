def introduction():
    print("Welcome to Fort Boyard!")
    print("The player(s) must complete challenges to earn keys and unlock the treasure room.")
    print("The aim is to collect three keys to access")

def create_dico():
    dico = {}

def compose_equipe(n):
    d={}
    for i in range(n):
    name=input("What is your name? ")
    profession=input("What is your profession? ")
        leader=input("Are you the leader? ")

def challenges_menu():
    l=["Mathematics challenge","Logic challenge","Chance challenge","Père Fouras'riddle"]
    for i in range (4):
        print(i+1, l[i])
    choice=int(input(("Choose your challenge by entering the number corresponding to your choice:")))
    while (choice>4 or choice<1):
        choice=int(input(("Invalid input, enter another number:")))
    return(l[choice-1])

def choose_player(team):
    print()

challenges_menu()



