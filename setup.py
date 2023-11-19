
from setuptools import setup, find_packages

with open('VERSION', 'r') as file:
    version = file.read()

with open('README.md') as file:
    long_description = file.read()

setup(
    name='llama_processor',
    version=version,
    packages=find_packages(),
    url=''
    license='MIT',
    author='Balakrishna Maduru',
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.10',
    package_data={'llama_processor': ['VERSION']},
)
