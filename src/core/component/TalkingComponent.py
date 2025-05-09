from pathlib import Path


from .Component import Component


class TalkingComponent(Component):
    def __init__(self, content: str):
        self.content = content

        super().__init__(element_uuid=self.content)

    def render_narration(self):
        return self.narration_template.render(content=self.content)

    def render_visual(self):
        return self.visual_template.render(content=self.content)

    def generate_elements(self, cached_component_dir_path: Path):
        pass
