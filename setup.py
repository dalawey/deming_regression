from setuptools import setup, find_packages

setup(
    name="deming_regression",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
    ],
    author="Dalawey Chen",
    description="A package for performing Deming regression",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/dalawey/deming_regression.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)