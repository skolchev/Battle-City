from Tank import Tank, TankType
from Config import TANK_WIDTH, TANK_HEIGHT, ARMOR_TANK_SPEED, ARMOR_TANK_ARMOR, ARMOR_TANK_ATTACK
from Resources import ARMOR_TANK_UP, ARMOR_TANK_RIGHT, ARMOR_TANK_DOWN, ARMOR_TANK_LEFT


class ArmorTank(Tank):

    # self, x, y, width, height, resources, speed, armor, attack, object_id, lives, type
    def __init__(self, x, y):
        super(ArmorTank, self).__init__(x, y, TANK_WIDTH, TANK_HEIGHT, 
            ARMOR_TANK_DOWN, ARMOR_TANK_SPEED, ARMOR_TANK_ARMOR, ARMOR_TANK_ATTACK, 0, 1, TankType.ARMOR)

    def move_up(self):
        self.resources = ARMOR_TANK_UP
        super(ArmorTank, self).move_up()

    def move_right(self):
        self.resources = ARMOR_TANK_RIGHT
        super(ArmorTank, self).move_right()

    def move_down(self):
        self.resources = ARMOR_TANK_DOWN
        super(ArmorTank, self).move_down()

    def move_left(self):
        self.resources = ARMOR_TANK_LEFT
        super(ArmorTank, self).move_left()
        