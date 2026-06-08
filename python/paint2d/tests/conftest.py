import os
import pytest

os.environ["SDL_VIDEODRIVER"] = "dummy"

import pygame


@pytest.fixture(scope="session", autouse=True)
def init_pygame():
    """Automatically initialize pygame components needed for testing."""
    pygame.init()
    yield
    pygame.quit()
