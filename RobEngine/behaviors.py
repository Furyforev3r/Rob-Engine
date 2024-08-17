from .sprite import Sprite
from .log import logger
from .input import Input
from .physics import Physics
from .types import locals


class SolidGroup:
    def __init__(self):
        self.group: list[Sprite] = []

    def add_sprite(self, sprite: Sprite):
        try:
            self.group.append(sprite)

        except Exception as error:
            logger.error(f"ERROR: {error}")


class EightDirections:
    """8 directions default behavior."""

    def __init__(
        self,
        character: Sprite,
        input_handler: Input,
        physics: Physics,
        solid_group: SolidGroup,
        speed: float = 1.0,
        enabled: bool = True,
    ):
        self.character = character
        self.input_handler = input_handler
        self.physics = physics
        self.solid_group = solid_group
        self.speed = speed
        self.velocity_x = 0
        self.velocity_y = 0
        self.enabled = enabled
        logger.info(f"{character} - 8 directions was assigned to the character.")

    def set_enabled(self, enabled: bool):
        try:
            logger.info(f"({self.character}) - Eight Directions set enabled: {enabled}")
            self.enabled = enabled

        except Exception as error:
            logger.error(f"ERROR: {error}")

    def setup_moviment(self):
        try:
            if self.enabled:
                self.velocity_x = 0
                self.velocity_y = 0

                if self.input_handler.is_pressed(locals.K_LEFT):
                    self.velocity_x = -self.speed
                if self.input_handler.is_pressed(locals.K_RIGHT):
                    self.velocity_x = self.speed
                if self.input_handler.is_pressed(locals.K_UP):
                    self.velocity_y = -self.speed
                if self.input_handler.is_pressed(locals.K_DOWN):
                    self.velocity_y = self.speed

                self.character.rect.x += self.velocity_x
                self.character.rect.y += self.velocity_y

                for solid_sprite in self.solid_group.group:
                    if self.physics.check_collisions(self.character, solid_sprite):
                        self.character.rect.x -= self.velocity_x
                        self.character.rect.y -= self.velocity_y
                        break

        except Exception as error:
            logger.error(f"ERROR: {error}")


class PlatformerMovement:
    """Platformer movement behavior."""

    def __init__(
        self,
        character: Sprite,
        input_handler: Input,
        physics: Physics,
        solid_group: SolidGroup,
        gravity: float = 0.1,
        jump_strength: float = 5.0,
        speed: float = 1.5,
        max_fall_speed: float = 10.0,
        enabled: bool = True,
    ):
        self.character = character
        self.input_handler = input_handler
        self.physics = physics
        self.solid_group = solid_group
        self.gravity = gravity
        self.jump_strength = jump_strength
        self.speed = speed
        self.max_fall_speed = max_fall_speed
        self.velocity_x = 0
        self.velocity_y = 0
        self.enabled = enabled
        self.on_ground = False
        logger.info(f"{character} - Platformer movement was assigned to the character.")

    def set_enabled(self, enabled: bool):
        try:
            logger.info(
                f"({self.character}) - Platformer Movement set enabled: {enabled}"
            )
            self.enabled = enabled

        except Exception as error:
            logger.error(f"ERROR: {error}")

    def apply_gravity(self):
        if not self.on_ground:
            self.velocity_y += self.gravity
            if self.velocity_y > self.max_fall_speed:
                self.velocity_y = self.max_fall_speed

    def jump(self):
        if self.on_ground:
            self.velocity_y = -self.jump_strength
            self.on_ground = False

    def setup_moviment(self):
        try:
            if self.enabled:
                self.velocity_x = 0

                if self.input_handler.is_pressed(locals.K_UP):
                    self.jump()
                if self.input_handler.is_pressed(locals.K_LEFT):
                    self.velocity_x = -self.speed
                if self.input_handler.is_pressed(locals.K_RIGHT):
                    self.velocity_x = self.speed

                self.apply_gravity()

                self.character.rect.x += self.velocity_x
                self.character.rect.y += self.velocity_y

                self.on_ground = False
                for solid_sprite in self.solid_group.group:
                    if self.physics.check_collisions(self.character, solid_sprite):
                        if self.velocity_y > 0:
                            self.character.rect.bottom = solid_sprite.rect.top
                            self.velocity_y = 0
                            self.on_ground = True
                        elif self.velocity_y < 0:
                            self.character.rect.top = solid_sprite.rect.bottom
                            self.velocity_y = 0
                        elif self.velocity_x != 0:
                            if self.velocity_x > 0:
                                self.character.rect.right = solid_sprite.rect.left
                            elif self.velocity_x < 0:
                                self.character.rect.left = solid_sprite.rect.right
                        break

        except Exception as error:
            logger.error(f"ERROR: {error}")
