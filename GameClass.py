import pygame as pg
import sys
import time


class Game:
    def __init__(self):

        self.width = 720
        self.height = 480

        self.red = pg.Color(255, 0, 0)
        self.green = pg.Color(0, 255, 0)
        self.blue = pg.Color(0, 0, 255)
        self.white = pg.Color(255, 255, 255)
        self.black = pg.Color(0, 0, 0)

        self.fps_controller = pg.time.Clock()

        self.score = 0

    def init_and_checks_errors(self):

        errors = pg.init()
        if errors[1] > 0:
            sys.exit(0)
        else:
            print("OK")

    def set_display(self):

        self.play_surface = pg.display.set_mode((self.width, self.height))
        pg.display.set_caption("Space War")

    def event_loop(self):
        pg.event.pump()
        change_to = "NOTHING"
        key = pg.key.get_pressed() # {D:True, A: False }
        
        if key[pg.K_RIGHT] or key[pg.K_d]:
            change_to = "RIGHT"
        elif key[pg.K_LEFT] or key[pg.K_a]:
            change_to = "LEFT"
        elif key[pg.K_ESCAPE]:
            sys.exit(0)

        return change_to

    def refresh_screen(self):
        pg.display.update()
        self.fps_controller.tick(60)

