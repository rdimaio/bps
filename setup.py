"""Setup for the project."""
from setuptools import setup

setup(
    name="sembps",
    version=1.0,
    description="Modified basis point set (BPS) library for semantic segmentation tasks",
    setup_requires=["numpy", "sklearn", "tqdm"],
    install_requires=[
        "sklearn",
        "tqdm",
        "numpy"
    ],
    author="Riccardo Di Maio, Sergey Prokudin",
    license="MIT-0",
    author_email="ramdimaio@gmail.com, prokus@amazon.com",
    packages=["sembps"]
)