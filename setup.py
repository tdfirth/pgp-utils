import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pgp-utils",
    version="1.0.1",
    author="Tom Firth",
    description="A small utility to wrap up common pgp/yubikey operations.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tdfirth/pgp-utils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={"console_scripts": ["pgp-utils=src.pgp_utils:main"]},
)
