from GameObject import GameObject
from Direction import Direction


class MovingObject(GameObject):

    def __init__(self, x, y, width, height, resources, speed, object_id):
        GameObject.__init__(self, x, y, width, height, resources, object_id)
        self.speed = speed
        self.direction = Direction.STILL
        self.orientation = Direction.STILL

    def move(self):
        if self.direction == Direction.UP:
            self.move_up()
        elif self.direction == Direction.RIGHT:
            self.move_right()
        elif self.direction == Direction.DOWN:
            self.move_down()
        elif self.direction == Direction.LEFT:
            self.move_left()
        else:
            pass

    def move_up(self):
        self.direction = Direction.UP
        self.orientation = Direction.UP
        super(MovingObject, self).move_up(self.speed)

    def move_down(self):
        self.direction = Direction.DOWN
        self.orientation = Direction.DOWN
        super(MovingObject, self).move_down(self.speed)

    def move_left(self):
        self.direction = Direction.LEFT
        self.orientation = Direction.LEFT
        super(MovingObject, self).move_left(self.speed)

    def move_right(self):
        self.direction = Direction.RIGHT
        self.orientation = Direction.RIGHT
        super(MovingObject, self).move_right(self.speed)
