from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name="pydsb",
    version="1.2.0",
    description="Unofficial DSBmobile API written in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    author="Lucas Hild",
    author_email="contact@lucas-hild.de",
    url="https://lucas-hild.de",
    py_modules=["pydsb"],
    install_requires=[
        "requests",
        "bs4"
    ],
)
