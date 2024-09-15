import pygame

from ..bll.base_character import BaseCharacter


class Player(BaseCharacter):
    def __init__(self, display):
        super().__init__(display)
        self.sprites = self.load_character_sprites("MarioIsaac/assets/sprites/base_character/my_base_character_v2.png", [48, 48, 48, 48, 48, 48], [48, 48, 48, 48, 48, 48], [12, 12, 8, 8, 8, 8])
        self.image = self.sprites["idle_down_right"][0]
        self.current_state = "idle"
        self.current_x_direction = "right"
        self.current_y_direction = "down"
        self.current_frame_index = 0
        self.speed = 5
        self.last_pressed_direction = None
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

    def _increment_frame(self):
        self.current_frame_index += 1
        total_frames = self.frame_counts.get(self.current_state, 5) * (self.sprite_frames.get(self.current_state, 12) - 1)
        if self.current_frame_index > total_frames:
            self.current_frame_index = 0

    def _apply_mask(self):
        self.mask = pygame.mask.from_surface(self.image)

    def _select_idle_image(self):
        frame_count = self.frame_counts.get("idle", 12)
        if self.current_y_direction == "up":
            self.image = self.sprites["idle_up"][self.current_frame_index // frame_count]
        else:
            if self.current_x_direction == "right":
                self.image = self.sprites["idle_down_right"][self.current_frame_index // frame_count]
            elif self.current_x_direction == "left":
                self.image = self.sprites["idle_down_left"][self.current_frame_index // frame_count]

    def _select_run_image(self):
        frame_count = self.frame_counts.get("run", 8)
        if self.current_y_direction == "up":
            self.image = self.sprites["run_up"][self.current_frame_index // frame_count]
        else:
            if self.current_x_direction == "right":
                self.image = self.sprites["run_down_right"][self.current_frame_index // frame_count]
            elif self.current_x_direction == "left":
                self.image = self.sprites["run_down_left"][self.current_frame_index // frame_count]

    def _select_attack_image(self):
        frame_count = self.frame_counts.get("attack", 8)
        if self.current_y_direction == "up":
            self.image = self.sprites["attack_up"][self.current_frame_index // frame_count]
        else:
            if self.current_x_direction == "right":
                self.image = self.sprites["attack_down_right"][self.current_frame_index // frame_count]
            elif self.current_x_direction == "left":
                self.image = self.sprites["attack_down_left"][self.current_frame_index // frame_count]

    def _update_rectangle(self):
        old_center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = old_center
        # self.rect.inflate_ip(-40, -40)

    def _select_image(self):
        if self.current_state == "idle":
            self._select_idle_image()
        elif self.current_state == "run":
            self._select_run_image()
        elif self.current_state == "attack":
            self._select_attack_image()
        self._update_rectangle()

    def update_sprite(self):
        self._increment_frame()
        self._select_image()
        self._apply_mask()

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
