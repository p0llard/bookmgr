import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bookmgr",  # Replace with your own username
    version="0.0.1",
    author="James Pollard",
    author_email="james@pollard-net.co.uk",
    description="A simple eBook manager",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/p0llard/bookmgr",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["pyyaml>=5.1"],
    entry_points={"console_scripts": ["bookmgr = bookmgr:main"],},
)
