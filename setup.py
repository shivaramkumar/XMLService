from setuptools import setup, find_packages

setup(
    name="xml_service",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "pydantic",
        "lxml",
        "sqlalchemy",
        "pytest",
    ],
)
