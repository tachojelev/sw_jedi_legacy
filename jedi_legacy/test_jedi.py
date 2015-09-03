from jedi import Jedi
import unittest


class TestJedi(unittest.TestCase):
    def setUp(self):
        self.player = Jedi("Obi-Wan")
        self.other = Jedi("Yoda")

    def test_init(self):
        self.assertEqual(self.player.name, "Obi-Wan")

    def test_getter_setter_name(self):
        self.player.name = "Luke"
        self.assertEqual(self.player.name, "Luke")

    def test_getter_setter_health(self):
        self.player.health = 55
        self.assertEqual(self.player.health, 55)

    def test_getter_setter_force(self):
        self.player.force = 78
        self.assertEqual(self.player.force, 78)

    def test_getter_setter_lightsaber(self):
        self.player.lightsaber = 31
        self.assertEqual(self.player.lightsaber, 31)

    def test_getter_setter_agility(self):
        self.player.agility = 20
        self.assertEqual(self.player.agility, 20)

    def test_is_dead_1(self):
        self.player.health = 0
        self.assertTrue(self.player.is_dead())

    def test_is_dead_2(self):
        self.player.health = -3
        self.assertTrue(self.player.is_dead())

    def test_is_dead_3(self):
        self.player.health = 10
        self.assertFalse(self.player.is_dead())

    def test_is_win_1(self):
        self.player.force = 100
        self.assertTrue(self.player.is_win())

    def test_is_win_2(self):
        self.player.force = 40
        self.assertFalse(self.player.is_win())

    def test_is_win_3(self):
        self.player.health = -10
        self.assertFalse(self.player.is_win())

    def test_operator__gt__1(self):
        self.player.force = 50
        self.player.lightsaber = 40
        self.player.agility = 30
        self.other.force = 45
        self.other.lightsaber = 35
        self.other.agility = 25
        self.assertTrue(self.player > self.other)

    def test_operator__gt__2(self):
        self.player.force = 10
        self.player.lightsaber = 20
        self.player.agility = 30
        self.other.force = 10
        self.other.lightsaber = 20
        self.other.agility = 30
        self.assertFalse(self.player > self.other)

    def test_operator__gt__3(self):
        self.player.force = 11
        self.player.lightsaber = 22
        self.player.agility = 33
        self.other.force = 44
        self.other.lightsaber = 55
        self.other.agility = 66
        self.assertFalse(self.player > self.other)

    def test_meditate_1(self):
        self.player.force = 51
        self.player.health = 70
        self.player.meditate()
        self.assertEqual(self.player.health, 93)

    def test_meditate_2(self):
        self.player.force = 49
        self.player.health = 70
        self.player.meditate()
        self.assertEqual(self.player.health, 84)

    def test_use_force(self):
        self.player.health = 30
        self.player.agility = 30
        self.player.force = 30
        self.player.use_force()
        self.assertEqual(self.player.health,  20)
        self.assertEqual(self.player.agility, 40)
        self.assertEqual(self.player.force, 35)

    def test_use_lightsaber(self):
        self.player.health = 20
        self.player.agility = 20
        self.player.lightsaber = 20
        self.player.use_lightsaber()
        self.assertEqual(self.player.health, 0)
        self.assertEqual(self.player.agility,  10)
        self.assertEqual(self.player.lightsaber, 40)

if __name__ == '__main__':
    unittest.main()
