import pygame

from os.path import join


class LevelDesigner:
    def __init__(self, display):
        self.display = display
        self.tmx_map = {0: load_pygame(join("MarioIsaac", "assets", "background", "dungeon_tileset.tmx"))}
        self.tile_size = (64, 64)
        self.scale_size = self.tile_size
        self.assets_path = "MarioIsaac/assets/background/"
        self.all_sprites = pygame.sprite.Group()
        self._load_world_images()

    def _load_world_images(self):
        kerb_images = {}
        kerb_images['top_left'] = pygame.transform.scale(pygame.image.load(self.assets_path + "dungeon/top_left.png"), self.scale_size)
        kerb_images['top_right'] = pygame.transform.scale(pygame.image.load(self.assets_path + "dungeon/top_right.png"), self.scale_size)
        kerb_images['top_middle'] = pygame.transform.scale(pygame.image.load(self.assets_path + "dungeon/top_middle.png"), self.scale_size)
        kerb_images['bottom_left'] = pygame.transform.scale(pygame.image.load(self.assets_path + "dungeon/bottom_left.png"), self.scale_size)
        kerb_images['bottom_right'] = pygame.transform.scale(pygame.image.load(self.assets_path + "dungeon/bottom_right.png"), self.scale_size)
        kerb_images['bottom_middle'] = pygame.transform.scale(pygame.image.load(self.assets_path + "dungeon/bottom_middle.png"), self.scale_size)
        kerb_images['left_middle'] = pygame.transform.scale(pygame.image.load(self.assets_path + "dungeon/left_middle.png"), self.scale_size)
        kerb_images['right_middle'] = pygame.transform.scale(pygame.image.load(self.assets_path + "dungeon/right_middle.png"), self.scale_size)
        kerb_images['center'] = pygame.transform.scale(pygame.image.load(self.assets_path + "dungeon/center.png"), self.scale_size)
        kerb_images['base_left'] = pygame.transform.scale(pygame.image.load(self.assets_path + "dungeon/base_left.png"), self.scale_size)
        kerb_images['base_middle'] = pygame.transform.scale(pygame.image.load(self.assets_path + "dungeon/base_middle.png"), self.scale_size)
        kerb_images['base_right'] = pygame.transform.scale(pygame.image.load(self.assets_path + "dungeon/base_right.png"), self.scale_size)

        self.world_images = kerb_images
