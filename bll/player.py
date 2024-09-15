import pygame

from ..bll.base_character import BaseCharacter


class Player(BaseCharacter):
    def __init__(self, display):
        super().__init__(display)
        self.sprites = self.load_character_sprites("MarioIsaac/assets/sprites/base_character/my_base_character_v2.png", [48, 48, 48, 48, 48, 48], [48, 48, 48, 48, 48, 48], [12, 12, 8, 8, 8, 8])
        self.image = self.sprites["idle_down_right"][0]
        self.rect = self.image.get_rect()
        self.speed = 5
        self.attack_counter = 0
        self.frame_counts = {
            "idle": 12,
            "run": 8,
            "attack": 8,
        }
        self.sprite_frames = {
            "idle": 12,
            "run": 8,
            "attack": 8,
        }

    def update_current_state(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_w] or keys[pygame.K_s]:
            self.current_state = "run"
        elif self.current_state == "attack":
            self.attack_counter += 1
            if self.attack_counter == 10:
                self.attack_counter = 0
                self.current_state = "idle"
        else:
            self.current_state = "idle"

    def update(self):
        self.update_current_state()
        self.update_sprite()
