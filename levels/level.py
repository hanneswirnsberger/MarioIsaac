import pygame

from ..bll.player import Player
from ..bll.tile import Tile
from ..bll.goblin import Goblin


class Level:
    level_one = [
        "111111111111",
        "100000000001",
        "102000000001",
        "100000000001",
        "100000000001",
        "100000000001",
        "100000000001",
        "100000000301",
        "100000000001",
        "100000303001",
        "100000000001",
        "111111111111",
    ]

    def __init__(self, display):
        self.current_level = 1
        self.display = display
        self.all_sprites = pygame.sprite.Group()
        self.world_tiles = self.create_world_tiles()
        for tile in self.world_tiles:
            self.all_sprites.add(tile)
        self.initialise_player()
        self.initialise_goblins()
        self.all_sprites.add(self.player)
        for goblin in self.goblins:
            self.all_sprites.add(goblin)
        self.camera_offset_x = 0
        self.camera_offset_y = 0

    def initialise_goblins(self):
        goblins = []
        for y, rows in enumerate(self.level_one):
            for x, column in enumerate(rows):
                if column == "3":
                    goblin = Goblin(self.display)
                    goblin.rect = goblin.image.get_rect(
                        topleft=(x * 64, y * 64)
                    )
                    goblin.mask = pygame.mask.from_surface(goblin.image)
                    goblins.append(goblin)
        self.goblins = goblins

    def initialise_player(self):
        self.player = Player(self.display)
        if self.current_level == 1:
            for y, rows in enumerate(self.level_one):
                for x, column in enumerate(rows):
                    if column == "2":
                        self.player.rect = self.player.image.get_rect(
                            topleft=(x * 64, y * 64)
                        )
                        self.player.mask = pygame.mask.from_surface(self.player.image)

    def load_world_images(self):
        tile_one = pygame.image.load("MarioIsaac/assets/background/black.png")
        tile_one = pygame.transform.scale(tile_one, (64, 64))

        return tile_one

    def create_world_tiles(self):
        image = self.load_world_images()
        world_tiles = []
        for y, rows in enumerate(self.level_one):
            for x, column in enumerate(rows):
                if column == "1":
                    tile = Tile(self.display)
                    tile.image = image
                    tile.rect = tile.image.get_rect(topleft=(x * 64, y * 64))
                    world_tiles.append(tile)
                    tile.mask = pygame.mask.from_surface(tile.image)

        return world_tiles

    def update_camera(self):
        self.camera_offset_x = self.player.rect.centerx - self.display.get_width() // 2
        self.camera_offset_y = self.player.rect.centery - self.display.get_height() // 2

    def handle_vertical_collision(self):
        for tile in self.world_tiles:
            if pygame.sprite.collide_mask(self.player, tile):
                if self.player.last_pressed_direction == "down" and self.player.rect.bottom > tile.rect.top:
                    self.player.rect.bottom = tile.rect.top
                elif self.player.last_pressed_direction == "up" and self.player.rect.top < tile.rect.bottom:
                    self.player.rect.top = tile.rect.bottom

    def handle_horizontal_collision(self):
        for tile in self.world_tiles:
            if pygame.sprite.collide_mask(self.player, tile):
                if self.player.last_pressed_direction == "right" and self.player.rect.right > tile.rect.left:
                    self.player.rect.right = tile.rect.left
                elif self.player.last_pressed_direction == "left" and self.player.rect.left <  tile.rect.right:
                    self.player.rect.left = tile.rect.right

    def update(self):
        self.player.update()
        for goblin in self.goblins:
            goblin.update((self.player.rect.x, self.player.rect.y))
        self.handle_vertical_collision()
        self.handle_horizontal_collision()
        self.update_camera()

    def draw(self):
        self.display.fill((255, 255, 255))
        for sprite in self.all_sprites:
            if sprite == self.player:
                sprite.draw(self.camera_offset_x, self.camera_offset_y, True)
            else:
                sprite.draw(self.camera_offset_x, self.camera_offset_y)

        pygame.display.update()
