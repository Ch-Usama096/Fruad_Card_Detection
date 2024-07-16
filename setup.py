from setuptools import find_packages , setup
from typing import List

# Define the Code for the get requriment function
def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n" , "") for req in requirements]
    return requirements

# Define the Parameters for setup
setup(
name         =  "Fruad Card Detection",
version      =  "0.0.1",
author       =  "Usama Husnain",
author_email =  "usamahusnain096@gmail.com",
packages     =  find_packages(),
install_requires =  get_requirements("requirements.txt"),
)