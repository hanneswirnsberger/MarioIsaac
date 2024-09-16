import pygame


class CollisionHandler:
    def __init__(self):
        pass

    def _handle_vertical_collision(self):
        for tile in self.world_tiles:
            if pygame.sprite.collide_mask(self.player, tile):
                if self.player.last_pressed_direction == "down" and self.player.rect.bottom > tile.rect.top:
                    self.player.rect.bottom = tile.rect.top
                elif self.player.last_pressed_direction == "up" and self.player.rect.top < tile.rect.bottom:
                    self.player.rect.top = tile.rect.bottom

    def _handle_horizontal_collision(self):
        for tile in self.world_tiles:
            if pygame.sprite.collide_mask(self.player, tile):
                if self.player.last_pressed_direction == "right" and self.player.rect.right > tile.rect.left:
                    self.player.rect.right = tile.rect.left
                elif self.player.last_pressed_direction == "left" and self.player.rect.left <  tile.rect.right:
                    self.player.rect.left = tile.rect.right

    def _handle_goblin_collision(self):
        for goblin in self.goblins:
            for tile in self.world_tiles:
                if pygame.sprite.collide_mask(goblin, tile):
                    print("Collision between the goblin and the tile")

            if pygame.sprite.collide_mask(goblin, self.player):
                print("Collision between the golbin and the player")
                self.player.take_damage(goblin.attack_power)

            for other_goblin in self.goblins:
                if other_goblin is not goblin:
                    if pygame.sprite.collide_mask(goblin, other_goblin):
                        if goblin.rect.centerx < other_goblin.rect.centerx:
                            goblin.rect.right = other_goblin.rect.left
                        elif goblin.rect.centerx > other_goblin.rect.centerx:
                            goblin.rect.left = other_goblin.rect.right

    def handle_collisions(self):
        self._handle_vertical_collision()
        self._handle_horizontal_collision()
        self._handle_goblin_collision()
