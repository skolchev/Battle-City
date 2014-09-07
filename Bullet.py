from MovingObject import MovingObject
from Resources import BULLET_UP, BULLET_RIGHT, BULLET_DOWN, BULLET_LEFT
from Config import BULLET_WIDTH, BULLET_HEIGHT 


class Bullet(MovingObject):

    def __init__(self, x, y, speed, owner_id, attack, direction):
        # super(Bullet, self).__init__(x, y, width, height, resources, speed, object_id)
        super(Bullet, self).__init__(x, y, BULLET_WIDTH, BULLET_HEIGHT, BULLET_UP, speed, 0)
        self.owner_id = owner_id
        self.attack = attack
        self.direction = direction

    def move_up(self):
        self.resources = BULLET_UP
        super(Bullet, self).move_up()

    def move_right(self):
        self.resources = BULLET_RIGHT
        super(Bullet, self).move_right()

    def move_down(self):
        self.resources = BULLET_DOWN
        super(Bullet, self).move_down()

    def move_left(self):
        self.resources = BULLET_LEFT
        super(Bullet, self).move_left()
