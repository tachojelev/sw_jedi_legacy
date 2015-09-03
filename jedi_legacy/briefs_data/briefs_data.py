from briefs import Missions
import unittest


class TestBriefs(unittest.TestCase):
    def setUp(self):
        self.master = Missions.get_random_master()
        self.lord = Missions.get_random_lord()
        self.brief = Missions.get_random_brief()

    def test_get_master(self):
        self.assertIsInstance(self.master, tuple)

    def test_get_lord(self):
        self.assertIsInstance(self.lord, tuple)

    def test_get_brief(self):
        self.assertIsInstance(self.brief, str)

if __name__ == '__main__':
    unittest.main()
