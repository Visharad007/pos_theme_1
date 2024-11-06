from setuptools import setup, find_packages

setup(
    name='pos_theme',  # This should match the name of your app folder
    version='0.0.1',
    description='POS Theme for ERPNext',
    packages=find_packages(),  # Automatically finds the pos_theme package
    include_package_data=True,
)
