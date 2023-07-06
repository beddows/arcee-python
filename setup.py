import setuptools
from setuptools import find_packages
import re

with open("./arcee/__init__.py", 'r') as f:
    content = f.read()
    # from https://www.py4u.net/discuss/139845
    version = re.search(r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]', content).group(1)
    
with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    install_requires = fh.read().split('\n')


setuptools.setup(
    name="arcee-align",  
    version=version,
    author="Arcee",
    author_email="jacob@arcee.ai",
    description="The open source toolkit for finetuning and deploying LLMs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://arcee.ai/",
    install_requires=install_requires,
    packages=find_packages(exclude=("tests",)),
    extras_require={
        "dev": ["flake8", "black==22.3.0", "isort", "twine", "pytest", "wheel"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)