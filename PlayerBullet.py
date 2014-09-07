from Bullet import Bullet
from Config import PLAYER_BULLET_ID, PLAYER_ID, PLAYER_TANK_BULLET_SPEED


class PlayerBullet(Bullet):

    # self, x, y, speed, object_id, ownerID, attack

    def __init__(self, x, y, speed, attack, direction):
        super(PlayerBullet, self).__init__(
            x, y, PLAYER_TANK_BULLET_SPEED, PLAYER_ID, attack, direction)
        self.id = PLAYER_BULLET_ID
