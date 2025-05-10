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


def main():
    full_component_name = f"{component_name.capitalize()}Component"

    with open(
        Path.cwd().parent / "src" / "core" / "component" / "GreetingComponent.py",
        "r",
    ) as file:
        data = file.read()

    data = data.replace("GreetingComponent", full_component_name)

    target_path = (
        Path.cwd().parent
        / "src"
        / "core"
        / "component"
        / f"{component_name.capitalize()}Component.py"
    )
    tc.assertFalse(
        target_path.exists(),
    )

    with open(
        target_path,
        "w",
    ) as file:
        file.write(data)

    shutil.copytree(
        Path.cwd().parent / "src" / "template" / "component" / "GreetingComponent",
        Path.cwd().parent / "src" / "template" / "component" / full_component_name,
    )

    print(
        f"Created {component_name.capitalize()}Component",
    )

    # add the component to the __init__.py file
    with open(
        Path.cwd().parent / "src" / "core" / "component" / "__init__.py",
        "r",
    ) as file:
        data = file.read()

    data = data.replace(
        "__all__ = [",
        f"""from .{full_component_name} import {full_component_name}

__all__ = [""",
    )

    data = data.replace(
        "]",
        f""""{full_component_name}",
]""",
    )

    with open(
        Path.cwd().parent / "src" / "core" / "component" / "__init__.py",
        "w",
    ) as file:
        file.write(data)


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(
        description="Scaffold for creating a new component in the src/core/component directory and src/template directory.",
    )
    arg_parser.add_argument(
        "--component_name",
        type=str,
    )
    args = arg_parser.parse_args()
    component_name = args.component_name

    tc.assertFalse(
        component_name.lower().endswith("component"),
    )

    main()
