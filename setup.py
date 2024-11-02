from setuptools import setup, find_packages
from typing import List

HYPEN_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_DOT in requirements:
            requirements.remove(HYPEN_DOT)

    return requirements

setup(
    name="Xray image classification",
    version="0.0.1",
    author="sayan",
    author_email="sayanghosh1489@gmail.com",
    install_requires=get_requirements(r"D:\Projects\deeplearningproject\requirements_dev.txt"),
    packages=find_packages()
)
