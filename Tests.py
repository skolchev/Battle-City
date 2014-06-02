import unittest
from Main import Tank, PlayerTank

class TestTank(unittest.TestCase):

    def setUp(self):
        self.tank = PlayerTank(0, 0)

    def test_move_down(self):
        self.tank.moveDown()
        self.assertEqual(self.tank.position(), (0, 3))

    def test_move_up(self):
        self.tank.moveUp()
        self.assertEqual(self.tank.position(), (0, -3))

    def test_move_left(self):
        self.tank.moveLeft()
        self.assertEqual(self.tank.position(), (-3, 0))

    def test_move_right(self):
        self.tank.moveRight()
        self.assertEqual(self.tank.position(), (0, 3))


if __name__ == '__main__':
    unittest.main()