from Rectangle import Rectangle


class GameObject(Rectangle):

    GAME_OBJECT_ID = 1000

    def __init__(self, x, y, width, height, resources, object_id=0):
        Rectangle.__init__(self, x, y, width, height)
        self.resources = resources
        self.is_destroyed = False

        if object_id != 0:
        	self.id = object_id
        else:
        	self.id = GameObject.GAME_OBJECT_ID
        	GameObject.GAME_OBJECT_ID += 1
