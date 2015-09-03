from person_data.person import Person


class Sith(Person):
    def meditate(self):
        if self.force > 50:
            self.health += self.health/5
        else:
            self.health += self.health/10

    def use_force(self):
        self.health -= 20
        self.agility += 15
        self.force += 10

    def use_lightsaber(self):
        self.health -= 10
        self.agility -= 20
        self.lightsaber += 30
