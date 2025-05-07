from .Component import Component


class NewspaperComponent(Component):
    def __init__(self, url: str):
        self.url = url

        super().__init__()

    def render_narration(self):
        return self.narration_template.render(url=self.url)

    def render_visual(self):
        return self.visual_template.render(url=self.url)

    