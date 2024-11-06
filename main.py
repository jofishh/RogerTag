import pygame as pg
import math, sys


class Game:
    def __init__(self):
        pg.init()
        self.width = game_settings.width
        self.height = game_settings.height
        self.screen = pg.display.set_mode((self.width, self.height))
        pg.display.set_caption("RogTag")
        self.running = True
        self.clock = pg.time.Clock()

    def handle_events(self): 
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def run(self):
        while self.running:
            self.handle_events()
            self.screen.fill((0, 0, 0))
            pg.display.flip()
            self.clock.tick(game_settings.FPS)
        pg.quit()

game = Game()
game.run()