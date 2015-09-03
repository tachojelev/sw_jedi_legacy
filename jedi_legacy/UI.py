from world import *


def game():
    print("----- WELCOME TO STAR WARS JEDI LEGACY! -----\n",
          "Please select your way of the force!\n",
          "(j)edi or (s)ith ?")
    choice = ""
    while choice != 'j' and choice != 's':
        choice = input("-> ")
    name = input("Enter your name: ")

    if choice == 'j':
        player = Jedi(name)
    else:
        player = Sith(name)

    world = World(player)
    world.intro()

if __name__ == '__main__':
    game()
