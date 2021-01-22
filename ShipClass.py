import pygame as pg


class Ship:
    def __init__(self, ship_color):

        self.position = [360, 400]
        self.ship_size = [30, 30]
        self.velocity = 2

        self.ship_color = ship_color

        self.move_direction = "NOTHING"

    def change_position(self):

        if self.move_direction == "NOTHING":
            return
        elif self.move_direction == "RIGHT":
            self.position[0] += self.velocity
        elif self.move_direction == "LEFT":
            self.position[0] -= self.velocity

    def draw_ship(self, play_surface, surface_color):
        play_surface.fill(surface_color)
        pg.draw.rect(
            play_surface,
            self.ship_color,
            pg.Rect(
                self.position[0], self.position[1],
                self.ship_size[0], self.ship_size[1]
            )
        )

    def check_for_boundaries(self, screen_width):
        if self.position[0] > screen_width - self.ship_size[0]:
            self.position[0] = screen_width - self.ship_size[0]
        elif self.position[0] < 0:
            self.position[0] = 0

