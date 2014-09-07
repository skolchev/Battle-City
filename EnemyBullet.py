from Bullet import Bullet
from Config import ENEMY_BULLET_ID, ENEMY_ATTACK


class EnemyBullet(Bullet):

    def __init__(self, x, y, speed, ownerID, direction):
        # (self, x, y, speed, objectID, ownerID, attack)
        super(EnemyBullet, self).__init__(x, y, speed, ENEMY_BULLET_ID, ownerID, ENEMY_ATTACK)
        self.direction = direction