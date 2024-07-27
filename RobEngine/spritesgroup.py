from pygame import sprite
from .log import logger
from .sprite import Sprite


class SpriteGroup:
    """SpriteGroup default class."""

    def __init__(self):
        self.SpriteGroup = sprite.Group()

    def add_sprite(self, sprite: Sprite):
        """Add a sprite to sprite group."""
        try:
            self.SpriteGroup.add(sprite)
            logger.info("Sprite added to group.")

        except Exception as error:
            logger.error(f"ERROR: {error}")

    def update(self):
        """Update all sprites in sprite group."""
        try:
            self.SpriteGroup.update()
        except Exception as error:
            logger.error(f"ERROR: {error}")
