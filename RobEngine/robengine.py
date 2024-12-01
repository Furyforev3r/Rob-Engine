from pygame import display, time, init, event
from .log import logger


class RobEngine:
    """The game screen default class.
    You can initialize project, modify window details and change scenes."""

    def __init__(
        self,
        display_caption: str = "Welcome to Rob Engine!",
        display_size: list[int] = [1280, 720]
    ):
        self.display_caption = display_caption
        self.display_size = display_size
        self.display = display
        self.screen = display.set_mode(display_size)
        display.set_caption(display_caption)
        self.event = event
        self.clock = time.Clock()

        logger.info(f"Display caption defined: {display_caption}")
        logger.info(f"Display size defined: {display_size}")
        logger.info("=== Game Screen initialized! ===")

    def initialize(self):
        """Initialize all imported modules."""
        try:
            init()
            logger.info("All modules initialized.")
        except Exception as error:
            logger.error(f"ERROR: {error}")

    def update(self, background_color: tuple[int, int, int,] = (0, 0, 0)):
        """Update the full display surface to the screen."""
        try:
            display.flip()
            self.screen.fill(background_color)
        except Exception as error:
            logger.error(f"ERROR: {error}")

    def change_display(self, display_size: list[int]):
        """Change display size."""
        try:
            self.display.set_mode(display_size)
            logger.info("Display changed.")
        except Exception as error:
            logger.error(f"ERROR: {error}")
