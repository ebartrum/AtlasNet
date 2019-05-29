from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["pandas", "visdom", "torch", "torchvision"]

setup(
    name="AtlasNet",
    version="0.1",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/ThibaultGROUEIX/AtlasNet",
    packages=['AtlasNet'],
    install_requires=requirements,
)
