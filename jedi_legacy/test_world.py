from world import *
import unittest


class TestWorld(unittest.TestCase):
    def setUp(self):
        self.player = Jedi("John Doe")
        self.world = World(self.player)

    def test_reset_score(self):
        self.player.health = 0
        self.player.force = 0
        self.player.lightsaber = 0
        self.player.agility = 0
        self.world.reset_score()
        self.assertEqual(self.player.health, 100)
        self.assertEqual(self.player.force, 10)
        self.assertEqual(self.player.lightsaber, 10)
        self.assertEqual(self.player.agility, 60)

    def test_is_game_over_1(self):
        self.player.force = 100
        self.player.health = 20
        self.assertTrue(self.world.is_game_over())

    def test_is_game_over_2(self):
        self.player.force = 80
        self.player.health = 0
        self.assertTrue(self.world.is_game_over())

    def test_is_game_over_3(self):
        self.player.force = 100
        self.player.health = 0
        self.assertTrue(self.world.is_game_over())

if __name__ == '__main__':
    unittest.main()
