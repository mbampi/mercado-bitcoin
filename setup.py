import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mercado-bitcoin",
    version="1.0.0",
    author="Matheus Dussin Bampi",
    author_email="matheusbampi@gmail.com",
    description="API Client in Python for Mercado Bitcoin",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=['bitcoin', 'trade', 'data', 'finance'],
    url="https://github.com/mbampi/mercado-bitcoin",
    install_requires=['requests'],
    packages=setuptools.find_packages(),
    package_dir={'': 'src'},
    classifiers=[
        'Development Status :: 4 - Beta'
        'Intended Audience :: Developers'
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)