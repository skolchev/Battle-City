from Tank import Tank, TankType
from Resources import PLAYER_UP, PLAYER_RIGHT, PLAYER_DOWN, PLAYER_LEFT
from Config import TANK_WIDTH, TANK_HEIGHT, PLAYER_TANK_SPEED, \
PLAYER_TANK_ARMOR, PLAYER_TANK_ATTACK, PLAYER_ID, PLAYER_LIVES
from Direction import Direction


class PlayerTank(Tank):

    def __init__(self, x, y):
        super(PlayerTank, self).__init__(
            x, y, TANK_WIDTH, TANK_HEIGHT, PLAYER_UP,
            PLAYER_TANK_SPEED, PLAYER_TANK_ARMOR, PLAYER_TANK_ATTACK,
            PLAYER_ID, PLAYER_LIVES, TankType.PLAYER)
        self.orientation = Direction.UP

    def move_up(self):
        self.resources = PLAYER_UP
        super(PlayerTank, self).move_up()

    def move_right(self):
        self.resources = PLAYER_RIGHT
        super(PlayerTank, self).move_right()

    def move_down(self):
        self.resources = PLAYER_DOWN
        super(PlayerTank, self).move_down()

    def move_left(self):
        self.resources = PLAYER_LEFT
        super(PlayerTank, self).move_left()
