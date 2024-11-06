# setup.py
from setuptools import setup, find_packages

setup(
    name='pos_theme',  # Ensure this matches the app folder name
    version='0.0.1',
    description='Your theme app for ERPNext',
    packages=find_packages(),
    include_package_data=True,
)
