from Tank import Tank, TankType
from Config import TANK_WIDTH, TANK_HEIGHT, POWER_TANK_SPEED, POWER_TANK_ARMOR, POWER_TANK_ATTACK
from Resources import POWER_TANK_UP, POWER_TANK_RIGHT, POWER_TANK_DOWN, POWER_TANK_LEFT


class PowerTank(Tank):

    # self, x, y, width, height, resources, speed, armor, attack, object_id, lives, type
    def __init__(self, x, y):
        super(PowerTank, self).__init__(x, y, TANK_WIDTH, TANK_HEIGHT, 
            POWER_TANK_DOWN, POWER_TANK_SPEED, POWER_TANK_ARMOR, POWER_TANK_ATTACK, 0, 1, TankType.POWER)

    def move_up(self):
        self.resources = POWER_TANK_UP
        super(PowerTank, self).move_up()

    def move_right(self):
        self.resources = POWER_TANK_RIGHT
        super(PowerTank, self).move_right()

    def move_down(self):
        self.resources = POWER_TANK_DOWN
        super(PowerTank, self).move_down()

    def move_left(self):
        self.resources = POWER_TANK_LEFT
        super(PowerTank, self).move_left()
from Tank import Tank, TankType
from Config import TANK_WIDTH, TANK_HEIGHT, POWER_TANK_SPEED, POWER_TANK_ARMOR, POWER_TANK_ATTACK
from Resources import POWER_TANK_UP, POWER_TANK_RIGHT, POWER_TANK_DOWN, POWER_TANK_LEFT


class PowerTank(Tank):

    # self, x, y, width, height, resources, speed, armor, attack, object_id, lives, type
    def __init__(self, x, y):
        super(PowerTank, self).__init__(x, y, TANK_WIDTH, TANK_HEIGHT, 
            POWER_TANK_DOWN, POWER_TANK_SPEED, POWER_TANK_ARMOR, POWER_TANK_ATTACK, 0, 1, TankType.POWER)

    def move_up(self):
        self.resources = POWER_TANK_UP
        super(PowerTank, self).move_up()

    def move_right(self):
        self.resources = POWER_TANK_RIGHT
        super(PowerTank, self).move_right()

    def move_down(self):
        self.resources = POWER_TANK_DOWN
        super(PowerTank, self).move_down()

    def move_left(self):
        self.resources = POWER_TANK_LEFT
        super(PowerTank, self).move_left()
