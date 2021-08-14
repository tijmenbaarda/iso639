import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="iso639-lang",
    version="0.3.1",
    author="L.Beaudoux",
    description="A lightweight library for the ISO 639 standard.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/l-bdx/iso639",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
    ],
    python_requires=">=3.6",
    package_data={"iso639": ["data/*.json"]},
)
