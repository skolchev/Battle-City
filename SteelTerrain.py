from Terrain import Terrain
from Config import TERRAIN_WIDTH, TERRAIN_HEIGHT, STEEL_ID, STEEL_ARMOR
from Resources import STEEL


class SteelTerrain(Terrain):

    def __init__(self, x, y):
        # self, x, y, width, height, resources, objectID, armor
        super(SteelTerrain, self).__init__(x, y, TERRAIN_WIDTH, TERRAIN_HEIGHT, STEEL, STEEL_ID, STEEL_ARMOR)