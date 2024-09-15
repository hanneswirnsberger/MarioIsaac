import pygame

from ..bll.tile import Tile


class MovingTile(Tile):
    def __init__(
        self, display, width: int = 100, height: int = 100, x: int = 10, y: int = 10
    ):
        self.speed = 0
        super().__init__(display)
        self.display_width, self.display_height = display.get_size()
        self.last_pressed_direction = None

    def move(self, dx, dy):
        self.update_old_rect()
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed
