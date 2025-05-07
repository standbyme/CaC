import sys
import unittest
from pathlib import Path

tc = unittest.TestCase()


def add_proj_to_PYTHONPATH():
    cwd = Path().cwd()
    assert cwd.name == "workdir"
    sys.path.insert(0, str(cwd.parent))


add_proj_to_PYTHONPATH()
from src.core.component.NewspaperComponent import NewspaperComponent


def main():
    component = NewspaperComponent(
        url="""https://www.propublica.org/article/the-secret-irs-files-trove-of-never-before-seen-records-reveal-how-the-wealthiest-avoid-income-tax""",
    )

    print(component)


if __name__ == "__main__":
    main()
