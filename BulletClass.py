import pygame as pg


class Bullet:

    def __init__(self, bullet_color,
                 offset):

        self.bullets = []
        self.timeRate = 2

        self.bullet_color = bullet_color
        self.bullet_size = (10, 10)
        self.bullet_offset = offset

        self.speed = 10   ### velocity

    def create_bullet(self, play_surface, x, y):
        bullet = pg.draw.rect(
            play_surface,
            self.bullet_color,
            pg.Rect(
                x + self.bullet_offset[0], y - self.bullet_offset[1],
                self.bullet_size[0], self.bullet_size[1]
            )
        )
        
        self.bullets.insert(0, bullet)

    def move_all_bullets(self, play_surface):

        for index, bullet in enumerate(self.bullets[:]):
            if bullet.y < 0:
                self.bullets.remove(bullet)
                continue
            self.bullets[index] = bullet.move(0, -self.speed)
            pg.draw.rect(
                play_surface,
                self.bullet_color,
                self.bullets[index]
            )
            # print(len(self.bullets))


