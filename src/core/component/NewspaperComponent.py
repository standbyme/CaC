import hashlib
import random
from pathlib import Path

import numpy as np
from PIL import Image

from .Component import Component


def generate_random_png(width, height, filename="random_image.png"):
    """Generates a random RGB PNG image and saves it to a file."""
    array = np.random.randint(0, 256, size=(height, width, 3), dtype=np.uint8)
    image = Image.fromarray(array)
    image.save(filename)


class NewspaperComponent(Component):
    def __init__(self, url: str):
        super().__init__()

        self.url = url
        encoded_string = self.url.encode("utf-8")
        hash = hashlib.md5(encoded_string).hexdigest()

        cache_dir = Path().cwd() / "cache"
        cache_dir.mkdir(parents=True, exist_ok=True)

        cached_component_dir_path = cache_dir / f"{hash}"
        if not cached_component_dir_path.exists():
            cached_component_dir_path.mkdir(parents=True, exist_ok=False)
            generate_random_png(
                128, 128, filename=cached_component_dir_path / "cover.png"
            )

        component_dir_path = Path().cwd() / f"{self.uuid}"
        component_dir_path.symlink_to(
            cached_component_dir_path, target_is_directory=True
        )

    def render_narration(self):
        return self.narration_template.render(url=self.url)

    def render_visual(self):
        return self.visual_template.render(url=self.url)
