import pygame

from ..bll.base_character import BaseCharacter


class Goblin(BaseCharacter):
    def __init__(self, display):
        super().__init__(display)
        self.sprites = self.load_character_sprites("MarioIsaac/assets/sprites/orcs/goblin.png", [48, 48, 48, 48, 64, 64], [48, 48, 48, 48, 64, 64], [4, 4, 8, 8, 10, 10])
        self.image = self.sprites["idle_down_right"][0]
        self.rect = self.image.get_rect()
