from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="bank_package",
    version="0.0.1",
    author="Bruno Ávila",
    author_email="avilabruno@live.com",
    description=" ",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/avilabrun/pacotes-python.git",
    packages=find_packages(),
    install_requirements=requirements,
    python_requires=">=3.9.13"
)