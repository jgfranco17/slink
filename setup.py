"""
Python setup.py for Slink package.
"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="slink",
    version=read("slink", "VERSION"),
    description="Python package for classic data structures",
    url="https://github.com/jgfranco17/slink/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="jgfranco17",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    extras_require={"test": read_requirements("requirements-test.txt")}
)
