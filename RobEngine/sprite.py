from pygame import image, Surface, sprite, transform
from .log import logger


class Sprite(sprite.Sprite):
    """The default sprite class."""

    def __init__(self, image_path: str, position: list[int]):
        super().__init__()
        self.image = image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.left = position[0]
        self.rect.top = position[1]

        logger.info("Sprite image loaded.")
        logger.info("Sprite rect defined")
        logger.info(f"Position set to {position}")

    def set_position(self, x: int, y: int):
        """Update position of the sprite."""
        try:
            self.rect.x = x
            self.rect.y = y
            logger.info(f"Position set to [{y, x}]")

        except Exception as error:
            logger.error(f"ERROR: {error}")

    def resize(self, size):
        try:
            self.image = transform.scale(self.image, size)
            self.rect = self.image.get_rect(topleft=self.rect.topleft)
        except Exception as error:
            logger.error(f"ERROR: {error}")

    def draw(self, screen: Surface):
        """Draw the sprite on the screen."""
        try:
            screen.blit(self.image, self.rect)
            logger.info("Drawn sprite.")
        except Exception as error:
            logger.error(f"ERROR: {error}")
