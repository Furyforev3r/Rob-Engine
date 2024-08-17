from .types import locals
from .log import logger
from pygame import key
from pygame.event import Event
from typing import Any


class Input:
    """Default input system."""

    def keydown(self):
        """Returns the pressed keys."""
        try:
            return locals.KEYDOWN
        except Exception as error:
            logger.error(f"ERROR: {error}")

    def keyup(self):
        """Returns the keys that have been released."""
        try:
            return locals.KEYUP
        except Exception as error:
            logger.error(f"ERROR: {error}")

    def get_pressed(self):
        """Returns the keys that are pressed down."""
        try:
            return key.get_pressed()
        except Exception as error:
            logger.error(f"ERROR: {error}")

    def is_pressed(self, key: int):
        """Compares if the key has been pressed down."""
        try:
            keys: Any = self.get_pressed()

            if keys[key]:
                return True

            return False
        except Exception as error:
            logger.error(f"ERROR: {error}")

    def was_pressed(self, key: int, event: Event):
        """Compares whether a key was pressed."""
        try:
            if event.type == locals.KEYDOWN and event.key == key:
                return True

            return False
        except Exception as error:
            logger.error(f"ERROR: {error}")
