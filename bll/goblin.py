import pygame

from ..bll.base_character import BaseCharacter


class Goblin(BaseCharacter):
    def __init__(self, display):
        super().__init__(display)
        self.sprites = self.load_character_sprites("MarioIsaac/assets/sprites/orcs/goblin.png", [48, 48, 48, 48, 64, 64], [48, 48, 48, 48, 64, 64], [4, 4, 8, 8, 8, 8])
        self.image = self.sprites["idle_down_right"][0]
        self.current_state = "idle"
        self.current_x_direction = "right"
        self.current_y_direction = "down"
        self.current_frame_index = 0
        self.frame_counts = {
            "idle": 4,
            "run": 8,
            "attack": 8,
        }
        self.sprite_frames = {
            "idle": 4,
            "run": 8,
            "attack": 8,
        }
        self.speed = 1
        self.attack_range = 20

    def move_to_player(self, player_pos):
        if player_pos[0] < self.rect.x:
            x_direction = -1
            self.current_x_direction = "left"
        elif player_pos[0] > self.rect.x:
            x_direction = 1
            self.current_x_direction = "right"
        else:
            x_direction = 0

        if player_pos[1] < self.rect.y:
            y_direction = -1
            self.current_y_direction = "up"
        elif player_pos[1] > self.rect.y:
            y_direction = 1
            self.current_y_direction = "down"
        else:
            y_direction = 0
        self.move(x_direction, y_direction)
        self.current_state = "run"

    def is_in_attack_range(self, player_pos):
        in_range = False
        if abs(self.rect.x - player_pos[0]) <= self.attack_range:
            in_range = True
        elif abs(self.rect.y - player_pos[1]) <= self.attack_range:
            in_range = True
        return in_range


    def update(self, player_pos):
        self.move_to_player(player_pos)
        if self.is_in_attack_range(player_pos):
            self.attack()
        self.update_sprite()
