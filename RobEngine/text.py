from typing import Any
import pygame
from .log import logger


class Text:
    """Default text system."""

    def __init__(
        self,
        text: str,
        font_name: Any = None,
        font_size: int = 30,
        color: tuple = (255, 255, 255),
    ):
        try:
            self.font = pygame.font.SysFont(font_name, font_size)
            self.text = text
            self.color = color
            self.surface = self.font.render(self.text, True, self.color)
        except Exception as error:
            logger.error(f"ERROR: {error}")

    def update_text(self, new_text: str):
        try:
            self.text = new_text
            self.surface = self.font.render(self.text, True, self.color)
        except Exception as error:
            logger.error(f"ERROR: {error}")

    def draw(self, screen: pygame.Surface, position: tuple):
        try:
            screen.blit(self.surface, position)
        except Exception as error:
            logger.error(f"ERROR: {error}")

    def set_color(self, new_color: tuple):
        try:
            self.color = new_color
            self.surface = self.font.render(self.text, True, self.color)
        except Exception as error:
            logger.error(f"ERROR: {error}")

    def set_font(self, font_name: str, font_size: int):
        try:
            self.font = pygame.font.SysFont(font_name, font_size)
            self.surface = self.font.render(self.text, True, self.color)
        except Exception as error:
            logger.error(f"ERROR: {error}")
