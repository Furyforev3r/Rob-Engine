from pygame import image, Surface
from .log import logger


class Sprite:
    """The default sprite class."""

    def __init__(self, image_path: str, position: list[int]):
        self.image = image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.left = position[0]
        self.rect.top = position[1]

    def set_position(self, x, y):
        """Update position of the sprite."""
        try:
            self.rect.x = x
            self.rect.y = y
        except Exception as error:
            logger.error(f"ERROR: {error}")

    def draw(self, screen: Surface):
        """Draw the sprite on the screen."""
        try:
            screen.blit(self.image, self.rect)
        except Exception as error:
            logger.error(f"ERROR: {error}")
