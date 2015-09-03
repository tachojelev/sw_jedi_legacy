from jedi import Jedi
from sith import Sith
from briefs_data.briefs import Missions
from random import randint
import sys
import time


class World:
    def __init__(self, player):
        self.__player = player
        self.__kind = ""
        if isinstance(player, Jedi):
            self.__kind = "jedi"
        else:
            self.__kind = "sith"

    def intro(self):
        print("Greetings, {0}!".format(self.__kind),
              "We wish you the best of luck and may the force be with you!")
        self.mission_1()

    def victory(self):
        print("Congratulations, you brought balance to the force and WON!")
        self.new_game()

    def defeat(self):
        print("You did not bring balance to the force and LOST!")
        self.new_game()

    def reset_score(self):
        self.__player.health = 100
        self.__player.force = 10
        self.__player.lightsaber = 10
        self.__player.agility = 60

    def new_game(self):
        print("Would you like to play another game? The galaxy needs you!\n")
        choice = ""
        while choice != 'y' and choice != 'n':
            choice = input("(y)es / (n)o\n")
        if choice == 'y':
            self.reset_score()
            self.intro()
        else:
            print("Too bad! This program will be closed in ...")
            self.countdown(5)
            sys.exit()

    def game_over(self):
        print("---------------- GAME OVER ----------------")
        if self.__player.is_dead():
            self.defeat()
        elif self.__player.is_win():
            self.victory()

    def is_game_over(self):
        return self.__player.is_dead() or self.__player.is_win()

    def is_ready(self):
        print("Type 'r' when you are ready to proceed with next mission!")
        while input() != 'r':
            pass

    def countdown(self, seconds):
        for i in range(0, seconds):
            print(seconds - i)
            time.sleep(1)

    def mission_1(self):
        seconds = abs(self.__player.agility//3)
        num = (randint(1, 15), randint(1, 5), randint(1, 10), randint(1, 15))
        key = num[0] // num[1] + num[2] * num[3]

        self.__player.show_stats()
        print(Missions.get_random_brief(),
              "You will have {0} seconds to answer".format(seconds),
              "\nType 'r' and press Enter when you're ready!")

        while input() != 'r':
            pass

        print("Calculate: ",
              num[0], " / ", num[1], " + ", num[2], " * ", num[3])
        start = time.time()
        choice = input("-> ")
        end = time.time()
        if end - start > seconds:
            print("--------- Out of time! ---------")
        elif choice != str(key):
            print("--------- Incorrect! ---------")
        else:
            print("--------- Correct! ---------")
            self.__player.agility += 5
            self.__player.force += 5
            self.__player.lightsaber += 5

        if self.is_game_over():
            self.game_over()
        else:
            self.is_ready()
            self.mission_2()

    def mission_2(self):
        seconds = self.__player.agility//3
        matrix = (randint(1, 9), randint(1, 1), randint(1, 9), randint(1, 9))
        key = matrix[0] * matrix[3] - matrix[1] * matrix[2]

        self.__player.show_stats()
        print(Missions.get_random_brief(),
              "You will have {0} seconds to answer".format(seconds),
              "\nType 'r' and press Enter when you're ready!")

        while input() != 'r':
            pass

        print("Calculate the determinante of the matrix A:\n",
              "(", matrix[0], " ", matrix[1], ")\n",
              "(", matrix[2], " ", matrix[3], ")")
        start = time.time()
        choice = input("-> ")
        end = time.time()
        if end - start > seconds:
            print("--------- Out of time! ---------")
        elif choice != str(key):
            print("--------- Incorrect! ---------")
        else:
            print("--------- Correct! ---------")
            self.__player.agility += 5
            self.__player.force += 5
            self.__player.lightsaber += 5

        if self.is_game_over():
            self.game_over()
        else:
            self.is_ready()
            self.mission_3()

    def mission_3(self):
        self.__player.show_stats()
        print("Be ware! You've been challenged to a duel!",
              "Don't hesitate and strike him down!",
              "\nWhat would you like to use in the fight?")

        choice = ""
        while choice != 'f' and choice != 'l':
            choice = input("(f)orce or (l)ightsaber -> ")

        if choice == 'f':
            self.__player.use_force()
        else:
            self.__player.use_lightsaber()

        sith = Sith("bad_guy")
        sith.force = self.__player.force * 2
        sith.agility = self.__player.agility//2

        self.countdown(3)
        if self.__player > sith:
            print("Fantastic job, you defeated him!")
        else:
            print("What a pity ... you've been killed!")
            self.__player.health = 0

        if self.is_game_over():
            self.game_over()
        else:
            self.is_ready()
            self.mission_4()

    def mission_4(self):
        self.__player.show_stats()
        opponent = ()
        if isinstance(self.__player, Jedi):
            opponent = Missions.get_random_master()
        else:
            opponent = Missions.get_random_lord()
        print(Missions.get_random_brief(),
              "The very {0} wants to test you!".format(opponent[0]),
              "You will be playing Rock, Paper, Scissors!",
              "So (r)ock, (p)aper or (s)cissors? Use the force!")

        choices = ('r', 'p', 's')
        choice1 = choices[randint(0, 2)]
        wins = (('r', 's'), ('p', 'r'), ('s', 'p'))

        choice2 = ''
        while choice2 != 'r' and choice2 != 'p' and choice2 != 's':
            choice2 = input("-> ")
        print("You: {0} // {1}: {2}".format(choice2, opponent[0], choice1))

        if choice1 == choice2:
            print("Interesting, a draw! Good job though!")
        elif (choice2, choice1) in wins:
            print("Extraordinary, you won! You will now meditate!")
            self.__player.meditate()
            self.countdown(3)
        else:
            print("You lost, but it happens. Next time perhaps!")
            self.__player.force -= 10
            self.__player.agility -= 10

        if self.is_game_over():
            self.game_over()
        else:
            self.is_ready()
            self.mission_5()

    def mission_5(self):
        self.__player.show_stats()
        helper = ()
        enemy = ()
        if isinstance(self.__player, Jedi):
            helper = Missions.get_random_master()
            enemy = Missions.get_random_lord()
        else:
            helper = Missions.get_random_lord()
            enemy = Missions.get_random_master()

        print(Missions.get_random_brief(),
              "You have just arrived at a distant planet in the Outer ring!",
              "{0} came with you to aid you if necessary!".format(helper[0]),
              "You are now browsing around ...")
        self.countdown(3)
        print("So unfortunate! {0} has followed you!".format(enemy[0]),
              "He's preparing to attack!",
              "Would you like to use {0}'s help?".format(helper[0]))

        choice = ""
        while choice != 'y' and choice != 'n':
            choice = input("(y)es or (n)o -> ")

        weapon = ""
        while weapon != 'f' and weapon != 'l':
            weapon = input("Use (f)orce or (l)ightsaber -> ")

        if choice == 'y' and self.__player.force + helper[1] >= enemy[1]:
            if weapon == 'f':
                self.__player.use_force()
            else:
                self.__player.use_lightsaber()
            print("Such a power you two unleashed, you defeated him!")
            self.__player.meditate()
            self.__player.force += 8
            self.__player.agility += 8
            self.__player.lightsaber += 8
        elif choice == 'y' and self.__player.force + helper[1] < enemy[1]:
            print("Unfortunately, even together you couldn't win!")
            self.__player.health = 0
        elif choice == 'n' and self.__player.force > enemy[1]:
            print("Great job young one, you defeated him!")
            self.__player.force += 20
            self.__player.agility += 20
            self.__player.lightsaber += 20
        else:
            print("You have been defeated!")
            self.__player.health = 0

        if self.is_game_over():
            self.game_over()
        else:
            self.is_ready()
            self.mission_6()

    def mission_6(self):
        self.__player.show_stats()
        helper = ()
        enemy = ()
        if isinstance(self.__player, Jedi):
            helper = Missions.get_random_master()
            enemy = Missions.get_random_lord()
        else:
            helper = Missions.get_random_lord()
            enemy = Missions.get_random_master()
        print(Missions.get_random_brief(),
              "A distress call has been sent by our masters",
              "Looks like our temple is under attack!",
              "You're with {0} and".format(helper[0]),
              "you've just arrived. FIGHT!")

        self.countdown(3)
        self.__player.use_lightsaber()
        self.__player.use_force()
        self.__player.meditate()

        print("You're gravely injured, but it's all or nothing!\n",
              "{0} is charging on you! What do you do?".format(enemy[0]),
              "(f)ight or (r)un")
        choice = ""
        while choice != 'f' and choice != 'r':
            choice = input("-> ")

        if choice == 'f' and self.__player.force >= enemy[1]:
            print("My god, you defeated him!")
            self.__player.force += 20
        elif choice == 'f' and self.__player.force < enemy[1]:
            print("You couldn't take it, you were killed!")
            self.__player.health = 0
        elif choice == 'r' and self.__player.force + helper[1] >= enemy[1]:
            print("{0} has joined you and helped you!".format(helper[0]),
                  "Your combined efforts defeated {0}".format(enemy[0]))
            self.__player.force += 8
        else:
            print("Both of you have perished!")
            self.__player.health = 0

        if self.is_game_over():
            self.game_over()
        else:
            self.is_ready()
            self.mission_7()

    def mission_7(self):
        self.__player.show_stats()
        print(Missions.get_random_brief(),
              "It all comes down to this, young warrior!",
              "We're making a full scale attack on the enemy's planet!",
              "Stick to your trainings and you might survive!",
              "Are you (r)eady?")
        while input("-> ") != 'r':
            pass
        self.countdown(3)

        n = (randint(1, 10), randint(1, 10), randint(1, 10))
        key = False
        if n[0] + n[1] > n[2] and n[1] + n[2] > n[0] and n[0] + n[2] > n[1]:
            key = True
        print("Does the following triangle exist? a = {0}, b = {1}, c = {2}?"
              .format(n[0], n[1], n[2]),
              "\n(y)es or (n)o")

        choice = ""
        while choice != 'y' and choice != 'n':
            choice = input("-> ")
        if (choice == 'y' and key) or (choice == 'n' and not key):
            print("Correct!")
            self.__player.force += 20
        else:
            print("Incorrect!")

        sq = randint(10, 20)
        print("Find x?   x^2 = {0}".format(sq**2))
        choice = input("-> ")
        if choice == str(sq):
            print("Correct!")
            self.__player.force += 20
        else:
            print("Incorrect!")

        if not self.__player.is_dead():
            print("You're covered in the blood of your enemies! Good job!")

        if self.is_game_over():
            self.game_over()
        else:
            self.is_ready()
            self.mission_1()
