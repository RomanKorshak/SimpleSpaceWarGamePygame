import pygame as pg


class Enemy:

    def __init__(self, enemy_color):

        self.enemy_size = (30, 30)
        self.velocity = 1

        self.enemy_color = enemy_color

        self.enemies = []
        self.timeRate = 7

    def create_enemy(self, play_surface, position):

        enemy = pg.draw.rect(
            play_surface,
            self.enemy_color,
            pg.Rect(
                position[0], position[1],
                self.enemy_size[0], self.enemy_size[1]
            )
        )

        self.enemies.insert(0, enemy)

    def move_all_enemies(self, play_surface, bullets, screen_height):

        index = 0

        for enemy in self.enemies[:]:

            if self.contains_collision(bullets, enemy):
                self.enemies.remove(enemy)
                index -= 1
                continue
            elif enemy.y > screen_height:
                self.enemies.remove(enemy)
                index -= 1
                continue
            self.enemies[index] = enemy.move(0, self.velocity)
            pg.draw.rect(
                play_surface,
                self.enemy_color,
                self.enemies[index]
            )
            index += 1

        # print(len(self.enemies))

    def contains_collision(self, bullets, enemy):

        for bullet in bullets[:]:
            if bullet.colliderect(enemy):
                return True
        return False