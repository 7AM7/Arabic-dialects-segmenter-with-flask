
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setup(
    name='FarasaPy3',
    version='3.0.0',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Farasa (which means “insight” in Arabic), is a fast and accurate text processing toolkit for Arabic text.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=['requests', 'json'],
    url='https://github.com/ahmed451/SummerInternship2020-PyPIFarasa/tree/master/7AM7',
    author='AM7',
    author_email='ahmed.moorsy798@gmail.com',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
