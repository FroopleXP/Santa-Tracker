import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="santa-tracker-frooplexp",
    version="1.0.0",
    author="Connor D. Edwards",
    author_email="connor@frooplexp.com",
    description="Basic Raspberry PI based Santa Tracker",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FroopleXP/Santa-Tracker",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Santa Tracker :: Google"
    ],
    python_requires='>=3.6',
)
