from person_data.person import Person


class Jedi(Person):
    def meditate(self):
        if self.force > 50:
            self.health += self.health//3
        else:
            self.health += self.health//5

    def use_force(self):
        self.health -= 10
        self.agility += 10
        self.force += 5

    def use_lightsaber(self):
        self.health -= 20
        self.agility -= 10
        self.lightsaber += 20
