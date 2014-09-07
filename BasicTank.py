from Tank import Tank, TankType
from Config import TANK_WIDTH, TANK_HEIGHT, BASIC_TANK_SPEED, BASIC_TANK_ARMOR, BASIC_TANK_ATTACK
from Resources import BASIC_TANK_UP, BASIC_TANK_RIGHT, BASIC_TANK_DOWN, BASIC_TANK_LEFT


class BasicTank(Tank):

    # self, x, y, width, height, resources, speed, armor, attack, object_id, lives, type
    def __init__(self, x, y):
        super(BasicTank, self).__init__(x, y, TANK_WIDTH, TANK_HEIGHT, 
            BASIC_TANK_DOWN, BASIC_TANK_SPEED, BASIC_TANK_ARMOR, BASIC_TANK_ATTACK, 0, 1, TankType.BASIC)

    def move_up(self):
        self.resources = BASIC_TANK_UP
        super(BasicTank, self).move_up()

    def move_right(self):
        self.resources = BASIC_TANK_RIGHT
        super(BasicTank, self).move_right()

    def move_down(self):
        self.resources = BASIC_TANK_DOWN
        super(BasicTank, self).move_down()

    def move_left(self):
        self.resources = BASIC_TANK_LEFT
        super(BasicTank, self).move_left()
        