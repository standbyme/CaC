from pathlib import Path

import numpy as np
from PIL import Image

from .Component import Component
from ..webdriver import screenshot


class NewspaperComponent(Component):
    def __init__(self, url: str):
        self.url = url

        super().__init__(element_uuid=self.url)

    def render_narration(self):
        return self.narration_template.render(url=self.url)

    def render_visual(self):
        return self.visual_template.render(url=self.url)

    def generate_elements(self, cached_component_dir_path: Path):
        screenshot(
            url=self.url,
            file_path=cached_component_dir_path / "screenshot.png",
        )
