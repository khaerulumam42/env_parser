
import setuptools
from utils.constant import VERSION

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='env_parser',  
     version=VERSION,
     scripts=['env_parser.py'],
     author="Khaerul Umam",
     author_email="khaery=ulumam42@gmail.com",
     description="utility package for parsing your secret env to example-format without show your credentials",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/khaerulumam42/env_parser",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )