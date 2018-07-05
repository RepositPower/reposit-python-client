import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Reposit Client",
    version="0.1",
    author="Thomas Basche",
    author_email="thomas.basche@repositpower.com",
    description="A library to communicate with a Reposit Controller",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tombasche/reposit",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License 2.0",
        "Operating System :: OS Independent",
    ),
)
