from GameClass import Game
from ShipClass import Ship
from BulletClass import Bullet

STEP = 0.1

game = Game()
ship = Ship(game.blue)
bullets = Bullet(game.green, (10, 15))


interval = bullets.timeRate
game.init_and_checks_errors()
game.set_display()

while True:
    ship.move_direction = game.event_loop()
    ship.change_position()

    ship.draw_ship(game.play_surface, game.white)

    if interval <= 0:
        bullets.create_bullet(game.play_surface, ship.position[0], ship.position[1])
        interval = bullets.timeRate
    else:
        interval -= STEP


    ship.check_for_boundaries(game.width)

    bullets.move_all_bullets(game.play_surface)

    game.refresh_screen()
