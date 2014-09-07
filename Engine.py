import random
import pygame
import sys
import time
from pygame.locals import *
from random import randint
from Config import *
from Resources import GAME_OVER, PLAYER_WINS
from Tank import TankType
from PlayerTank import PlayerTank
from BasicTank import BasicTank
from ArmorTank import ArmorTank
from FastTank import FastTank
from PowerTank import PowerTank
from Bullet import Bullet
from PlayerBullet import PlayerBullet
from BrickTerrain import BrickTerrain
from SteelTerrain import SteelTerrain
from Falcon import Falcon
from Direction import Direction
from Rectangle import Rectangle
from FieldConfig import LEVEL_1
from TankTypesConfig import TANK_TYPES_LEVEL_1
from GameObject import GameObject


def get_new_object_position(object):
    new_object_position = Rectangle(
        object.x, object.y, object.width, object.height)
    if object.direction == Direction.UP:
        new_object_position.y -= object.speed
    elif object.direction == Direction.RIGHT:
        new_object_position.x += object.speed
    elif object.direction == Direction.DOWN:
        new_object_position.y += object.speed
    elif object.direction == Direction.LEFT:
        new_object_position.x -= object.speed

    return new_object_position


def is_in_field(object):
    return object.x >= 0 and \
        object.x + object.width <= GAME_FIELD_WIDTH and \
        object.y >= 0 and \
        object.y + object.height <= GAME_FIELD_HEIGHT


def main():
    # Initialize game variables
    pygame.init()
    FPS_CLOCK = pygame.time.Clock()
    DISPLAY_SURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    BG_COLOR = (60, 60, 100)
    pygame.display.set_caption("Battle City")
    DISPLAY_SURF.fill(BG_COLOR)
    game_over = False
    player_wins = False

    # Create Field
    field = Rectangle(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)

    # Create Player Tank
    player_tank = PlayerTank(100, 100)

    # Create Terrain
    terrains = []
    for row in range(len(LEVEL_1)):
        for col in range(len(LEVEL_1[row])):
            if LEVEL_1[col][row] == BRICK_ID:
                terrains.append(
                    BrickTerrain(row * TERRAIN_WIDTH, col * TERRAIN_HEIGHT))
            elif LEVEL_1[col][row] == STEEL_ID:
                terrains.append(
                    SteelTerrain(row * TERRAIN_WIDTH, col * TERRAIN_HEIGHT))

    # Create Falcon
    falcon = Falcon(
        (GAME_FIELD_WIDTH / 2) - FALCON_WIDTH,
        (GAME_FIELD_HEIGHT - FALCON_HEIGHT))

    # Create bullets
    bullets = []

    # Create enemy tanks
    enemy_tanks = []
    directions = [Direction.STILL, Direction.UP,
                  Direction.RIGHT, Direction.DOWN, Direction. LEFT]
    created_tanks = 0
    destroyed_tanks = 0
    # tank_types = [TankType.PLAYER, TankType.BASIC,
    #               TankType.ARMOR, TankType.FAST, TankType.POWER]
    tank_types = [PlayerTank, BasicTank,
                  ArmorTank, FastTank, PowerTank]

    while not game_over:
        # 1. Handle Events

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        keystate = pygame.key.get_pressed()
        if keystate[K_UP]:
            player_tank.direction = Direction.UP
        elif keystate[K_DOWN]:
            player_tank.direction = Direction.DOWN
        elif keystate[K_RIGHT]:
            player_tank.direction = Direction.RIGHT
        elif keystate[K_LEFT]:
            player_tank.direction = Direction.LEFT

        player_bullets = [b for b in bullets if b.owner_id == PLAYER_ID]
        if keystate[K_SPACE]:
            if len(player_bullets) < PLAYER_FIRE_RATE:
                bullets.append(
                    PlayerBullet(player_tank.x, player_tank.y,
                                 5, 1, player_tank.orientation))

        # Create tanks
        if created_tanks < ENEMY_TANKS_TOTAL_COUNT and \
                len(enemy_tanks) < MAX_NUMBER_OF_TANKS_AT_ONCE:
            position = ENEMY_TANKS_START_POSITIONS[
                randint(0, len(ENEMY_TANKS_START_POSITIONS) - 1)]
            new_tank_position = Rectangle(
                position[0], position[1], TANK_WIDTH, TANK_HEIGHT)

            # Check if position is free
            is_free = True
            for tank in enemy_tanks:
                if new_tank_position.contains(tank):
                    is_free = False

            # Add new tank
            if is_free:
                # if TankType.BASIC == tank_types[
                #         TANK_TYPES_LEVEL_1[created_tanks]]:
                #     enemy_tanks.append(BasicTank(position[0], position[1]))
                # elif TankType.ARMOR == tank_types[
                #         TANK_TYPES_LEVEL_1[created_tanks]]:
                #     enemy_tanks.append(ArmorTank(position[0], position[1]))
                # elif TankType.FAST == tank_types[
                #         TANK_TYPES_LEVEL_1[created_tanks]]:
                #     enemy_tanks.append(FastTank(position[0], position[1]))
                # elif TankType.POWER == tank_types[
                #         TANK_TYPES_LEVEL_1[created_tanks]]:
                #     enemy_tanks.append(PowerTank(position[0], position[1]))

                enemy_tanks.append(
                    (tank_types[TANK_TYPES_LEVEL_1[created_tanks]])
                    (position[0], position[1]))
                created_tanks += 1

        # Change enemy tanks directions if they have collided
        # and fire if tanks haven't fired already
        bullets_owners = [b.owner_id for b in bullets]
        for enemy in enemy_tanks:
            if enemy.direction == Direction.STILL:
                enemy.direction = directions[randint(1, 4)]

            if enemy.id not in bullets_owners:
                bullets.append(
                    Bullet(enemy.x, enemy.y, BULLET_SPEED,
                           enemy.id, 1, enemy.direction))

        # -- End Handle Events

        # 2. Update Game State

        new_player_position = get_new_object_position(player_tank)
        # Handle Collisions
        if not is_in_field(new_player_position):
            player_tank.direction = Direction.STILL

        # Handle player collision with falcon
        if falcon.contains(new_player_position):
            player_tank.direction = Direction.STILL

        # Handle collision with terrain
        for terrain in list(terrains):

            # Handle collisions with bullets
            for bullet in list(bullets):
                if terrain.contains(bullet) and \
                        not terrain.is_destroyed and \
                        not bullet.is_destroyed:
                    bullet.is_destroyed = True
                    if isinstance(terrain, BrickTerrain):
                        terrain.armor -= 1
                        if terrain.armor <= 0:
                            terrain.is_destroyed = True

            # Handle collisions with player tank
            if terrain.contains(new_player_position):
                player_tank.direction = Direction.STILL

            # Handle collisions with enemy tanks
            for enemy in enemy_tanks:
                new_enemy_position = get_new_object_position(enemy)

                if terrain.contains(new_enemy_position):
                    enemy.direction = Direction.STILL

        # Handle collisions with enemy tanks
        for enemy in list(enemy_tanks):
            new_enemy_position = get_new_object_position(enemy)

            # Check if tank is within field
            if not is_in_field(new_enemy_position):
                enemy.direction = Direction.STILL

            # Handle collisions with falcon
            if falcon.contains(new_enemy_position):
                enemy.direction = Direction.STILL

            # Handle collisions with bullets
            for b in player_bullets:
                if enemy.contains(b) and \
                        not enemy.is_destroyed and \
                        not b.is_destroyed:
                    b.is_destroyed = True
                    enemy.armor -= 1
                    if enemy.armor <= 0:
                        enemy.is_destroyed = True
                        destroyed_tanks += 1

            # Handle collisions with other tanks
            for e in list(enemy_tanks):
                if e.id != enemy.id:
                    new_e_position = get_new_object_position(e)
                    if new_e_position.contains(new_enemy_position):
                        enemy.direction = Direction.STILL
                        e.direction = Direction.STILL

            # Handle collisions with player tank
            if new_enemy_position.contains(new_player_position):
                player_tank.direction = Direction.STILL
                enemy.direction = Direction.STILL

        # Handle collisions with bullets
        for bullet in list(bullets):
            new_bullet_position = get_new_object_position(bullet)

            # Check if bullet is within field
            if not is_in_field(new_bullet_position) and \
                    not bullet.is_destroyed:
                bullet.is_destroyed = True

            # Handle collisions with falcon
            if falcon.contains(new_bullet_position):
                bullet.is_destroyed = True
                falcon.is_destroyed = True
                game_over = True

            # Handle collisions with other bullets
            for b in player_bullets:
                if bullet.id != b.id and not bullet.is_destroyed \
                        and not b.is_destroyed:
                    if new_bullet_position.contains(b):
                        bullet.is_destroyed = True
                        b.is_destroyed = True

            # Handle collisions with player tank
            if bullet.owner_id != PLAYER_ID:
                if new_player_position.contains(new_bullet_position) and \
                        not bullet.is_destroyed and \
                        not player_tank.is_destroyed:
                    bullet.is_destroyed = True
                    player_tank.lives -= 1
                    if player_tank.lives <= 0:
                        player_tank.is_destroyed = True
                        game_over = True

        # Move Player
        # Check if any key is pressed
        if keystate[K_UP] or keystate[K_DOWN] \
                or keystate[K_RIGHT] or keystate[K_LEFT]:
            player_tank.move()

        # Remove destroyed enemies
        destroyed_enemies = [e for e in enemy_tanks if e.is_destroyed is True]
        for enemy in destroyed_enemies:
            enemy_tanks.remove(enemy)

        # Remove destroyed bullets
        destroyed_bullets = [b for b in bullets if b.is_destroyed is True]
        for bullet in destroyed_bullets:
            bullets.remove(bullet)

        # Remove destroyed terrains
        destroyed_terrains = [t for t in terrains if t.is_destroyed is True]
        for terrain in destroyed_terrains:
            terrains.remove(terrain)

        # Move enemies
        for enemy in enemy_tanks:
            enemy.move()

        # Move bullets
        for bullet in bullets:
            bullet.move()

        if destroyed_tanks >= ENEMY_TANKS_TOTAL_COUNT:
            player_wins = True

        # -- End Update Game State

        # 3. Draw Screen

        # Draw Background
        DISPLAY_SURF.fill(BG_COLOR)

        # Draw Terrain
        for terrain in terrains:
            DISPLAY_SURF.blit(
                pygame.image.load(terrain.resources), terrain.position())

        # Draw Player
        DISPLAY_SURF.blit(
            pygame.image.load(player_tank.resources), player_tank.position())

        # Draw Enemies
        for enemy in enemy_tanks:
            DISPLAY_SURF.blit(
                pygame.image.load(enemy.resources), enemy.position())

        # Draw Bullets
        for bullet in bullets:
            DISPLAY_SURF.blit(
                pygame.image.load(bullet.resources), bullet.position())

        # Draw Falcon
        DISPLAY_SURF.blit(
            pygame.image.load(falcon.resources), falcon.position())

        # You Win
        if player_wins:
            DISPLAY_SURF.blit(pygame.image.load(PLAYER_WINS), (100, 100))
            pygame.display.update()
            time.sleep(5)
            pygame.quit()
            sys.exit()

        # Exit game if falcon is dead or you have run out of lives
        if game_over:
            DISPLAY_SURF.blit(pygame.image.load(GAME_OVER), (250, 250))
            pygame.display.update()
            time.sleep(5)
            pygame.quit()
            sys.exit()

        # -- End Draw Screen

        pygame.display.update()
        FPS_CLOCK.tick(FPS)

if __name__ == '__main__':
    main()
