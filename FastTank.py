from Tank import Tank, TankType
from Config import TANK_WIDTH, TANK_HEIGHT, FAST_TANK_SPEED, FAST_TANK_ARMOR, FAST_TANK_ATTACK
from Resources import FAST_TANK_UP, FAST_TANK_RIGHT, FAST_TANK_DOWN, FAST_TANK_LEFT


class FastTank(Tank):

    # self, x, y, width, height, resources, speed, armor, attack, object_id, lives, type
    def __init__(self, x, y):
        super(FastTank, self).__init__(x, y, TANK_WIDTH, TANK_HEIGHT, 
            FAST_TANK_DOWN, FAST_TANK_SPEED, FAST_TANK_ARMOR, FAST_TANK_ATTACK, 0, 1, TankType.FAST)

    def move_up(self):
        self.resources = FAST_TANK_UP
        super(FastTank, self).move_up()

    def move_right(self):
        self.resources = FAST_TANK_RIGHT
        super(FastTank, self).move_right()

    def move_down(self):
        self.resources = FAST_TANK_DOWN
        super(FastTank, self).move_down()

    def move_left(self):
        self.resources = FAST_TANK_LEFT
        super(FastTank, self).move_left()
        