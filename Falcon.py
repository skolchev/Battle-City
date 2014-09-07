from GameObject import GameObject
from Config import FALCON_WIDTH, FALCON_HEIGHT, FALCON_ID
from Resources import FALCON


class Falcon(GameObject):

    # self, x, y, width, height, resources, object_id=0
    def __init__(self, x, y):
        super(Falcon, self).__init__(x, y, FALCON_WIDTH, FALCON_HEIGHT, FALCON, FALCON_ID)
