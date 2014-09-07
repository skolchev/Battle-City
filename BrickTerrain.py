from Terrain import Terrain
from Config import TERRAIN_WIDTH, TERRAIN_HEIGHT, BRICK_ID, BRICK_ARMOR
from Resources import BRICK


class BrickTerrain(Terrain):

    def __init__(self, x, y):
        # self, x, y, width, height, resources, objectID, armor
        super(BrickTerrain, self).__init__(x, y, TERRAIN_WIDTH, TERRAIN_HEIGHT, BRICK, BRICK_ID, BRICK_ARMOR)