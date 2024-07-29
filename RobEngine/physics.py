from .sprite import Sprite
from .log import logger
from pygame import Rect


class Physics:
    """Pyshics default module."""

    def update(self, entity: Sprite, gravity: int, dt: int):
        try:
            entity.rect.y -= gravity * dt
        except Exception as error:
            logger.error(f"ERROR: {error}")

    def check_collisions(self, entity_1: Sprite, entity_2: Sprite):
        try:
            entity_1_rect = Rect(entity_1.rect.topleft, entity_1.rect.size)
            entity_2_rect = Rect(entity_2.rect.topleft, entity_2.rect.size)

            verify = entity_1_rect.colliderect(entity_2_rect)

            return verify
        except Exception as error:
            logger.error(f"ERROR: {error}")
