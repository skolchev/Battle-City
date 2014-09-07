from GameObject import GameObject


class Terrain(GameObject):

    def __init__(self, x, y, width, height, resources, objectID, armor):
        super(Terrain, self).__init__(x, y, width, height, resources, objectID)
        self.armor = armor