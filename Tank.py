from MovingObject import MovingObject
import time


class TankType:
    PLAYER = 0
    BASIC = 1
    ARMOR = 2
    FAST = 3
    POWER = 4

class Tank(MovingObject):

    def __init__(self, x, y, width, height, resources, speed,
                 armor, attack, object_id, lives, type):
        super(Tank, self).__init__(
            x, y, width, height, resources, speed, object_id)
        self.armor = armor
        self.attack = attack
        self.lives = lives
        self.type = type
        self.move_time = 0
        self.move_timer = time.time()

    def move(self):
        self.move_time = time.time() - self.move_timer
        super(Tank, self).move()
