import unittest
from PlayerTank import PlayerTank
from ArmorTank import ArmorTank
from Tank import Tank
from Falcon import Falcon
from Terrain import Terrain
from BrickTerrain import BrickTerrain
from Bullet import Bullet
from Direction import Direction


class TestCollisions(unittest.TestCase):

    def setUp(self):
        self.player = PlayerTank(100, 100)

    def test_player_tank_collision_with_enemy_bullet(self):
        # x, y, speed, owner_id, attack, direction
        enemy_bullet = Bullet(86, 100, 5, 500, 1, Direction.RIGHT)
        self.assertFalse(self.player.contains(enemy_bullet))

        enemy_bullet.move()
        self.assertFalse(self.player.contains(enemy_bullet))

        enemy_bullet.move()
        self.assertTrue(self.player.contains(enemy_bullet))

    def test_player_tank_collision_with_brick(self):
        terrain = BrickTerrain(131, 100)

        self.assertFalse(terrain.contains(self.player))

        self.player.direction = Direction.RIGHT
        self.player.move()

        self.assertTrue(terrain.contains(self.player))

    def test_bullet_collision_with_brick(self):
        terrain = BrickTerrain(150, 150)
        enemy_bullet = Bullet(150, 141, 5, 500, 1, Direction.DOWN)

        self.assertFalse(terrain.contains(enemy_bullet))

        enemy_bullet.move();
        self.assertTrue(terrain.contains(enemy_bullet))

    def test_player_tank_collision_with_other_tank(self):
        other_tank = ArmorTank(100, 141)
        other_tank.direction = Direction.UP

        self.assertFalse(self.player.contains(other_tank))

        self.player.direction = Direction.DOWN
        self.player.move()
        other_tank.move()
        self.assertFalse(self.player.contains(other_tank))

        self.player.move()
        other_tank.move()
        self.assertTrue(self.player.contains(other_tank))

    def test_player_tank_collision_with_falcon(self):
        falcon = Falcon(100, 64)

        self.assertTrue(falcon.contains(self.player))

if __name__ == '__main__':
    unittest.main()
