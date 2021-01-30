from GameClass import Game
from ShipClass import Ship
from BulletClass import Bullet
from EnemyClass import Enemy
import random

STEP = 0.1

game = Game()
ship = Ship(game.blue)
bullets = Bullet(game.green, (10, 15))
enemies = Enemy(game.red)


bullet_interval = bullets.timeRate
enemy_interval = enemies.timeRate
game.init_and_checks_errors()
game.set_display()

while True:
    ship.move_direction = game.event_loop()
    ship.change_position()

    ship.draw_ship(game.play_surface, game.black)

    if enemy_interval <= 0:
        enemy_position = (random.randint(0, game.width - enemies.enemy_size[0]), 0)
        enemies.create_enemy(game.play_surface, enemy_position)
        enemy_interval = enemies.timeRate
    else:
        enemy_interval -= STEP

    if bullet_interval <= 0:
        bullets.create_bullet(game.play_surface, ship.position[0], ship.position[1])
        bullet_interval = bullets.timeRate
    else:
        bullet_interval -= STEP


    ship.check_for_boundaries(game.width)

    bullets.move_all_bullets(game.play_surface)
    enemies.move_all_enemies(game.play_surface, bullets.bullets, game.height)

    game.refresh_screen()
