from random import randint


class Missions(object):
    masters = (("Master Yoda", 90),
               ("Master Windu", 80),
               ("Master Plo Koon", 70),
               ("Master Shaak Ti", 65),
               ("Master Obi-Wan Kenobi", 75),
               ("Master Qui-Gon Jinn", 60))

    lords = (("Darth Sidious", 90),
             ("Darth Vader", 80),
             ("Darth Maul", 70),
             ("Darth Plagueis", 65),
             ("Darth Bane", 75),
             ("Darth Tyranus", 60))

    briefs = ("You must be the new apprentice, let's see what you've got!",
              "You came higly recommended by our masters, show me why!",
              "The force is inside all of us, but can you manage it?",
              "Anger leads to both suffering and power, remember that!",
              "Let's see if you can use both the force and the lightsaber!",
              "The force is strong with you, but you must prove yourself!",
              "With great power comes great responsibility, remember it!",
              "You are only as strong as your greatest weakness young one!",
              "The dark side of the force is a pathway to many abilities!",
              "After death, we all become one with the force!",
              "Our masters have given you an assignment, try and do well!",
              "Your mind and power are about to get twisted, get ready!",
              "Remember to always use the force with respect and humility!",
              "We've got a task for you, do your best to solve it!",
              "The more you train, the more powerful you will become!",
              "The force is the one thing all living things share in common!",
              "The lightsaber is a weapon tha combines our old and new ways!",
              "Think through the situation and don't rush into a battle!",
              "Opportunities must be created by you, young apprentice!",
              "Never lose your lightsaber, that weapon is your life!",
              "Both the dark side and the light side have their advantages!",
              "The war between light and darkness is one that is eternal!")

    @classmethod
    def get_random_master(cls):
        index = randint(0, 5)
        return cls.masters[index]

    @classmethod
    def get_random_lord(cls):
        index = randint(0, 5)
        return cls.lords[index]

    @classmethod
    def get_random_brief(cls):
        index = randint(0, 21)
        return cls.briefs[index]
