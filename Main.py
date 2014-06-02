import random, pygame, sys
from pygame.locals import *


class Tank:

    def __init__(self, tank_speed, bullet_speed, fire_rate, armor, points, x, y):
        self.tank_speed = tank_speed
        self.bullet_speed = bullet_speed
        self.fire_rate = fire_rate
        self.armor = armor
        self.points = points
        self.x = x
        self.y = y

    def fire(self):
        return 1

    def moveUp(self):
        self.y -= self.tank_speed

    def moveRight(self):
        self.x += self.tank_speed

    def moveDown(self):
        self.y += self.tank_speed

    def moveLeft(self):
        self.x -= self.tank_speed

    def position(self):
        return (self.x, self.y)


class BasicTank(Tank):

    def __init__(self, x, y):
        Tank.__init__(self, 3, 100, 100, 1, 100, x, y)


class FastTank(Tank):

    def __init__(self, x, y):
        Tank.__init__(self, 5, 100, 100, 1, 200, x, y)


class PowerTank(Tank):

    def __init__(self, x, y):
        Tank.__init__(self, 3, 130, 100, 1, 300, x, y)


class ArmorTank(Tank):

    def __init__(self, x, y):
        Tank.__init__(self, 3, 100, 100, 4, 400, x, y)


class PlayerTank(Tank):

    def __init__(self, x, y):
        Tank.__init__(self, 3, 100, 100, 1, 0, x, y)


FPS = 30
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
GAME_FIELD_WIDTH = 540
GAME_FIELD_HEIGHT = 405
TANK_WIDTH = 30
TANK_HEIGHT = 31


class ImageGallery:
    playerUp = 'Images\\Player-Up.png'
    playerRight = 'Images\\Player-Right.png'
    playerDown = 'Images\\Player-Down.png'
    playerLeft = 'Images\\Player-Left.png'

    armorTankUp = 'Images\\Armor-Tank-Up.png'
    armorTankRight = 'Images\\Armor-Tank-Right.png'
    armorTankDown = 'Images\\Armor-Tank-Down.png'
    armorTankLeft = 'Images\\Armor-Tank-Left.png'

    bricks = 'Images\\Bricks.png'


class Wall:

    def __init__(self, armor, x, y):
        self.armor = armor
        self.x = x
        self.y = y

    def position(self):
        return (self.x, self.y)


class Brick(Wall):

    def __init__(self, x, y):
        Wall.__init__(self, 4, x, y)


class Steel(Wall):

    def __init__(self, x, y):
        Wall.__init__(self, maxint, x, y)

class PowerUp:

    POINTS = 500

    def __init__(self):
        pass

class Granade(PowerUp):
    pass

class Helmet(PowerUp):
    pass

class Shovel(PowerUp):
    pass

class Star(PowerUp):
    pass

class TankLife(PowerUp):
    pass

class Timer(PowerUp):
    pass



def main():
    # Initialize game variables
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    BGCOLOR = (60, 60, 100)
    pygame.display.set_caption("Battle City")
    DISPLAYSURF.fill(BGCOLOR)

    # Initialize player variables
    NORMAL_SPEED = 3
    player = PlayerTank(15, 15)
    playerImg = pygame.image.load(ImageGallery.playerUp)

    # Initialize walls
    WALL_WIDTH = GAME_FIELD_WIDTH / 36
    WALL_HEIGHT = GAME_FIELD_HEIGHT / 36
    brickImg = pygame.image.load(ImageGallery.bricks)
    walls = [Brick(x, 0) for x in range(0, GAME_FIELD_WIDTH, 36)]

    while True:
        DISPLAYSURF.fill(BGCOLOR)
        DISPLAYSURF.blit(playerImg, player.position())

        for wall in walls:
            DISPLAYSURF.blit(brickImg, wall.position())

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Key states have nothing to do with the event queue - you are polling
        # the states of every key for every event in your queue. You need to
        # poll their states outside of your event-handling code.
        keystate = pygame.key.get_pressed()
        # Check if tank is within the screen
        if keystate[K_UP] and ((player.position()[1] - NORMAL_SPEED) >= 0):
            player.moveUp()
            playerImg = pygame.image.load(ImageGallery.playerUp)
        elif keystate[K_DOWN] and ((player.position()[1] + NORMAL_SPEED) < (GAME_FIELD_HEIGHT - TANK_HEIGHT + 3)):
            player.moveDown()
            playerImg = pygame.image.load(ImageGallery.playerDown)
        elif keystate[K_RIGHT] and ((player.position()[0] + NORMAL_SPEED) < (GAME_FIELD_WIDTH - TANK_WIDTH + 2)):
            player.moveRight()
            playerImg = pygame.image.load(ImageGallery.playerRight)
        elif keystate[K_LEFT] and ((player.position()[0] - NORMAL_SPEED) >= 0):
            player.moveLeft()
            playerImg = pygame.image.load(ImageGallery.playerLeft)

        pygame.display.update()
        FPSCLOCK.tick(FPS)


if __name__ == '__main__':
    main()
