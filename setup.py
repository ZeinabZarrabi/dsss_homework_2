from distutils.core import setup
from setuptools import find_packages

setup(
    name="math_quiz",
    version="0",
    author="Zeinab Zarrabi",
    author_email='zeinab.zarrabi@fau.de',
    packages=find_packages(),
    install_requires=["random"]
)