from setuptools import setup, find_packages

setup(
    name='u2net',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'torch',
        'torchvision',
        'Pillow',
        'numpy'
    ],
)
