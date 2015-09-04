class Person:
    def __init__(self, name):
        self._name = name
        self._health = 100
        self._force = 10
        self._lightsaber = 10
        self._agility = 60

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, health):
        self._health = health
        if self._health > 100:
            self._health = 100

    @property
    def force(self):
        return self._force

    @force.setter
    def force(self, force):
        self._force = force
        if self._force > 100:
            self._force = 100
        elif self._force < 0:
            self._force = 0

    @property
    def lightsaber(self):
        return self._lightsaber

    @lightsaber.setter
    def lightsaber(self, lightsaber):
        self._lightsaber = lightsaber
        if self._lightsaber > 100:
            self._lightsaber = 100
        elif self._lightsaber < 0:
            self._lightsaber = 0

    @property
    def agility(self):
        return self._agility

    @agility.setter
    def agility(self, agility):
        self._agility = agility
        if self._agility > 100:
            self._agility = 100
        elif self._agility < 10:
            self._agility = 10

    def is_dead(self):
        return self.health <= 0

    def is_win(self):
        return self.force >= 100

    def __gt__(self, other):
        power1 = self.force*0.4 + self.lightsaber*0.3 + self.agility*0.3
        power2 = other.force*0.4 + other.lightsaber*0.3 + other.agility*0.3
        return power1 > power2

    def show_stats(self):
        print(" ---------------------------------\n"
              "HP: {0} //".format(self.health),
              "Force: {0} //".format(self.force),
              "Lightsaber: {0} //".format(self.lightsaber),
              "Agility: {0}\n".format(self.agility),
              "---------------------------------")
