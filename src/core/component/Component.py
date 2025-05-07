import sys
import unittest
from abc import ABC, abstractmethod
from pathlib import Path

from jinja2 import Template

tc = unittest.TestCase()


def add_proj_to_PYTHONPATH():
    cwd = Path().cwd()
    assert cwd.name == "workdir"
    sys.path.insert(0, str(cwd.parent))


add_proj_to_PYTHONPATH()

src_path = Path().cwd().parent / "src"


class Component(ABC):
    def __init__(self):
        self.narration_template = self.get_template("narration")
        self.visual_template = self.get_template("visual")

        self.narration = self.render_narration()
        self.visual = self.render_visual()

    def get_template(self, name: str):
        class_name = self.__class__.__name__
        template_path = (
            Path(__file__).parent.parent.parent
            / "template"
            / "component"
            / class_name
            / f"{name}.jinja"
        )

        with open(template_path, "r") as f:
            template = Template(f.read())

        return template

    @abstractmethod
    def render_narration(self):
        raise NotImplementedError()

    @abstractmethod
    def render_visual(self):
        raise NotImplementedError()

    def __str__(self):
        return f"Component: {self.__class__.__name__}\nNarration: {self.narration}\nVisual: {self.visual}"
