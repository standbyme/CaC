import hashlib
import os
import platform
import shutil
import subprocess
import unittest
import uuid
from abc import ABC, abstractmethod
from pathlib import Path

from jinja2 import Template

tc = unittest.TestCase()

project_name = os.environ.get("PROJECT_NAME")
tc.assertIsNotNone(project_name)

project_dir_path = Path().cwd() / project_name


def create_link_to_directory(source: Path, target: Path):
    if not source.is_dir():
        raise ValueError(f"Source '{source}' is not a directory.")

    if target.exists():
        raise FileExistsError(f"Target '{target}' already exists.")

    system = platform.system()

    if system == "Linux":
        # Create symbolic link
        target.symlink_to(source, target_is_directory=True)
    elif system == "Windows":
        # Use PowerShell to create a junction
        command = f'New-Item -ItemType Junction -Path "{target}" -Target "{source}"'
        subprocess.run(["powershell", "-Command", command], check=True, shell=True)
    else:
        raise NotImplementedError(f"Unsupported OS: {system}")


class Component(ABC):
    def __init__(self, element_uuid: str):
        self.component_uuid = uuid.uuid4()

        self.element_uuid = element_uuid
        self.element_uuid_hash = hashlib.md5(
            self.element_uuid.encode("utf-8")
        ).hexdigest()

        self.narration_template = self.get_template("narration")
        self.visual_template = self.get_template("visual")

        cache_dir = Path().cwd() / "cache"
        cache_dir.mkdir(parents=True, exist_ok=True)
        cached_component_dir_path = cache_dir / f"{self.element_uuid_hash}"

        try:
            if not cached_component_dir_path.exists():
                cached_component_dir_path.mkdir(parents=True, exist_ok=False)
                self.generate_elements(cached_component_dir_path)

            project_dir_path.mkdir(parents=True, exist_ok=True)

            component_dir_path = project_dir_path / f"{self.component_uuid}"
            create_link_to_directory(cached_component_dir_path, component_dir_path)
        except:
            shutil.rmtree(cached_component_dir_path)
            raise

    @abstractmethod
    def generate_elements(self, cached_component_dir_path: Path):
        raise NotImplementedError()

    @abstractmethod
    def render_narration(self):
        raise NotImplementedError()

    @abstractmethod
    def render_visual(self):
        raise NotImplementedError()

    @property
    def narration(self):
        return self.render_narration()

    @property
    def visual(self):
        return self.render_visual()

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

    def __str__(self):
        return f"Component: {self.__class__.__name__}\nNarration: {self.narration}\nVisual: {self.visual}"
