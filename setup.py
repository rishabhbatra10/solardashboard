import os

from setuptools import setup, find_packages


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="solar-dashboard",
    version="1.0.1",
    author="Rishabh Batra",
    author_email="rishabh.batra@klassifai.com",
    description="Package to hold klassifai packages",
    license="Apache version 2.0",
    keywords="dashboard, PV",
    packages=find_packages(),
    include_package_data=True,
    long_description=read('README.md'),
    classifiers=[],
    install_requires=['pandas>=0.23.4', 'numpy>=1.15.1', 'Django==2.0.8', 'bokeh==0.13.0', 'django-pandas==0.5.1', 'django-model-utils>=1.4.0']
)
