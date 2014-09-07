import unittest
from MovingObject import MovingObject
from Direction import Direction


class TestMovingObject(unittest.TestCase):

    def setUp(self):
        self.moving_object = MovingObject(100, 100, 5, 5, "empty.png", 1, 1000)

    def test_move_up(self):
        self.moving_object.move_up()
        expected = (100, 99)
        self.assertEqual(self.moving_object.position(), expected)

    def test_move_right(self):
        self.moving_object.move_right()
        expected = (101, 100)
        self.assertEqual(self.moving_object.position(), expected)

    def test_move_down(self):
        self.moving_object.move_down()
        expected = (100, 101)
        self.assertEqual(self.moving_object.position(), expected)

    def test_move_left(self):
        self.moving_object.move_left()
        expected = (99, 100)
        self.assertEqual(self.moving_object.position(), expected)

    def test_move_according_direction(self):
        self.moving_object.direction = Direction.UP
        self.moving_object.move()
        self.assertEqual(self.moving_object.position(), (100, 99))

        self.moving_object.direction = Direction.RIGHT
        self.moving_object.move()
        self.assertEqual(self.moving_object.position(), (101, 99))

        self.moving_object.direction = Direction.DOWN
        self.moving_object.move()
        self.assertEqual(self.moving_object.position(), (101, 100))

        self.moving_object.direction = Direction.LEFT
        self.moving_object.move()
        self.assertEqual(self.moving_object.position(), (100, 100))

    def test_set_xy(self):
        self.moving_object.set_xy(19, 14)
        self.assertEqual(self.moving_object.position(), (19, 14))

if __name__ == '__main__':
    unittest.main()
