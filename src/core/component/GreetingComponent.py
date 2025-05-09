from pathlib import Path


from .Component import Component


class GreetingComponent(Component):
    def __init__(self):
        super().__init__(element_uuid="GreetingComponent")

    def render_narration(self):
        return self.narration_template.render()

    def render_visual(self):
        return self.visual_template.render()

    def generate_elements(self, cached_component_dir_path: Path):
        pass
