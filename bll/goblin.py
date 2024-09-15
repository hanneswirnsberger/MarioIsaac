import pygame

from ..bll.base_character import BaseCharacter


class Goblin(BaseCharacter):
    def __init__(self, display):
        super().__init__(display)
        self.sprites = self.load_character_sprites("MarioIsaac/assets/")
