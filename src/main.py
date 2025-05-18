import json
import os
import shutil
import sys
import unittest
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from dotenv import load_dotenv

assert load_dotenv()
tc = unittest.TestCase()


def add_proj_to_PYTHONPATH():
    cwd = Path().cwd()
    assert cwd.name == "workdir"
    sys.path.insert(0, str(cwd.parent))


add_proj_to_PYTHONPATH()
from src.core.component import *

project_name = os.environ.get("PROJECT_NAME")
tc.assertIsNotNone(project_name)

project_dir_path = Path().cwd() / project_name


def topic_to_text_script(topic: str):
    raise NotImplementedError()


def text_script_to_components(text_script: str):
    raise NotImplementedError()


def topic_to_AV_script(topic: str):
    # text_script = topic_to_text_script(topic)
    # components = text_script_to_components(text_script)
    # return components

    tc.assertEqual(
        topic,
        "How the rich avoid taxes?",
    )

    return [
        BeginningComponent(),
        TalkingComponent(
            "Today we are going to talk about how to legally avoid taxes."
        ),
        NewspaperComponent(
            "https://www.propublica.org/article/the-secret-irs-files-trove-of-never-before-seen-records-reveal-how-the-wealthiest-avoid-income-tax"
        ),
        TalkingComponent("This is a very interesting article."),
        EndComponent(),
    ]


def main():
    if project_dir_path.exists():
        shutil.rmtree(project_dir_path)

    topic = "How the rich avoid taxes?"

    AV_script = topic_to_AV_script(topic)

    for component in AV_script:
        component.generate()

    meta = {
        "topic": topic,
        "component_order": [component.component_uuid for component in AV_script],
    }

    with open(project_dir_path / "meta.json", "w") as f:
        f.write(json.dumps(meta, indent=4))


if __name__ == "__main__":
    main()
