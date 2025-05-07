import hashlib
import random
from pathlib import Path

import numpy as np
from PIL import Image

from .Component import Component


class NewspaperComponent(Component):
    def __init__(self, url: str):
        self.url = url

        super().__init__(element_uuid=self.url)

    def render_narration(self):
        return self.narration_template.render(url=self.url)

    def render_visual(self):
        return self.visual_template.render(url=self.url)

    def generate_elements(self, cached_component_dir_path: Path):
        array = np.random.randint(0, 256, size=(50, 50, 3), dtype=np.uint8)
        image = Image.fromarray(array)
        image.save(cached_component_dir_path / "image.png")
