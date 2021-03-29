import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="reposit",
    version="0.5.0",
    author="Thomas Basche",
    author_email="tcbasche@gmail.com",
    description="A library to communicate with a Reposit Controller",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RepositPower/reposit-python-client",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests',
        'six'
    ],
    classifiers=(
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ),
)
