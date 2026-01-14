"""
the setup.py file is an essential part of packaging and distributing
python projects. it is used by setuptools
or distutils in older python versions to define the configuration
of your project, such as its metadata,dependencies,and more
"""

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """

    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt', 'r') as file:
            #read lines from the file
            lines=file.readlines()
            #process each line
            for line in lines:
                requirement=line.strip()
                ##ignoreempty lines and -e .
                if requirement and requirement !='-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("requirments.txt file not found")

    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Harsh Raj Singh",
    author_email="rajsinghharsh1611@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)