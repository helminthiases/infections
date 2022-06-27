import setuptools

NAME = 'infections'
VERSION = '1.0.0'
DESCRIPTION = 'Masters Project'
AUTHOR = 'greyhypotheses'
URL = 'https://github.com/helminthiases/infections'
PYTHON_REQUIRES = '>=3.8'

with open('README.md') as f:
    readme = f.read()

setuptools.setup() (
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=readme,
    author=AUTHOR,
    url=URL,
    python_requires=PYTHON_REQUIRES,
    packages=setuptools.find_packages(exclude=['docs', 'tests'])
)