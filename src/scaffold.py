import argparse
import sys
import unittest
from pathlib import Path

from dotenv import load_dotenv
import shutil

assert load_dotenv()
tc = unittest.TestCase()


def add_proj_to_PYTHONPATH():
    cwd = Path().cwd()
    assert cwd.name == "workdir"
    sys.path.insert(0, str(cwd.parent))


def main():
    shutil.copyfile(
        Path.cwd().parent / "src" / "core" / "component" / "GreetingComponent.py",
        Path.cwd().parent
        / "src"
        / "core"
        / "component"
        / f"{component_name.capitalize()}Component.py",
    )

    shutil.copytree(
        Path.cwd().parent / "src" / "template" / "component" / "GreetingComponent",
        Path.cwd().parent
        / "src"
        / "template"
        / "component"
        / f"{component_name.capitalize()}Component",
    )

    print(
        f"Created {component_name.capitalize()}Component.",
    )


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(
        description="Scaffold for creating a new component in the src/core/component directory and src/template directory.",
    )
    arg_parser.add_argument(
        "component_name",
        type=str,
    )
    args = arg_parser.parse_args()
    component_name = args.component_name
