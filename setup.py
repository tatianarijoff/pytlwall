from setuptools import setup, find_packages, Extension

#########
# Setup #
#########


setup(
    name='pytlwall',
    version='1.0.0',
    description='Transmission line impedance calculation engine',
    url='',
    authors='Tatiana Rijoff and Carlo Zannini',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.0',
        ]
    )
